from typing import List
# Import the required libraries
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO (can change to DEBUG for more details)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define log message format
)

# Create a logger object
logger = logging.getLogger(__name__)


def classify_product(description: str, categories: List[str], model_name: str = "llama3.1") -> str:
    """
    Classifies a product description into one of the provided categories using an LLM.

    Args:
        description (str): A detailed product description to classify.
        categories (List[str]): A list of category labels to classify the product into.
        model_name (str): The name of the LLM model to use for classification. Default is "llama3.1".

    Returns:
        str: The predicted category for the product description.
    """
    # Create an instance of OllamaLLM with the specified model name
    llm = OllamaLLM(model=model_name)

    # Define the prompt template to instruct the LLM how to classify the product
    prompt_template = """
    You are an expert product classifier. Given the following product description and list of categories, choose the most appropriate category for the product.
    Since this output will be used by other automated processing, only respond with the category name that matches the product description.  

    Product Description: {description}

    Categories: {categories}

    The best category for the product is:
    """

    # Prepare the prompt template with placeholders for product description and categories
    prompt = ChatPromptTemplate.from_template(prompt_template)

    # Create the LLM chain that will run the prompt
    chain = LLMChain(llm=llm, prompt=prompt)

    # Format the categories list into a comma-separated string
    categories_str = ", ".join(categories)

    # Run the chain with the formatted input and capture the response from the model
    response = chain.run({
        "description": description,
        "categories": categories_str
    })

    # Log the input description, categories, and the output response for tracking purposes
    logger.info(f"Product Description: {description}")
    logger.debug(f"Category: {response.strip()}")
    logger.info(f"Model Response: {response}")

    # Return the classified category, stripping any extra whitespace
    return response.strip()


def classify_products(descriptions: List[str], categories: List[str]) -> List[str]:
    """
    Classifies multiple product descriptions into one of the provided categories.

    Args:
        descriptions (List[str]): A list of product descriptions to classify.
        categories (List[str]): A list of category labels to classify the products into.

    Returns:
        List[str]: A list of predicted categories for each product description.
    """
    results = []  # List to store the classification results

    # Loop through each product description and classify it
    for description in descriptions:
        result = classify_product(description, categories)  # Classify each product
        results.append(result)  # Store the result

        # Print the description and its classified category for easy tracking
        print(f"Description: {description} \n -> Classified as: {result}\n")

    # Return the list of classification results
    return results


if __name__ == "__main__":
    """
    Example execution of the classify_products function with predefined inputs.
    """

    # Example list of product descriptions to classify
    product_descriptions = [
        "A smartphone with 128GB storage and 6GB RAM.",  # Electronic product example
        "A comfortable cotton t-shirt, available in various colors.",  # Clothing product example
        "A blender with 3-speed settings and a glass jar.",  # Home appliance product example
    ]

    # Example categories that the products can be classified into
    categories = ["Electronics", "Clothing", "Home Appliances", "Sports Equipment", "Toys"]

    # Call the classify_products function and get the classification results
    classified_results = classify_products(product_descriptions, categories)

    # Output the results in a readable format
    for i, category in enumerate(classified_results):
        print(f"Product {i + 1}: {category}")
