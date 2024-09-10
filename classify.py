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
    # Create the Ollama LLM instance
    llm = OllamaLLM(model=model_name)
    prompt_template = """
    You are an expert product classifier. Given the following product description and list of categories, choose the most appropriate category for the product.
    Since this output will be used by other automated processing, only respond with the category name that matches the product description.  

    Product Description: {description}

    Categories: {categories}

    The best category for the product is:
    """

    # Prepare the prompt template
    prompt = ChatPromptTemplate.from_template(prompt_template)

    # Create the chain
    chain = LLMChain(llm=llm, prompt=prompt)

    # Format the categories into a comma-separated string
    categories_str = ", ".join(categories)

    # Run the chain to get the category
    response = chain.run({
        "description": description,
        "categories": categories_str
    })
    logger.info(description)
    logger.info(categories_str)
    logger.info(response)
    return response.strip()


def classify_products(descriptions: List[str], categories: List[str]) -> List[str]:
    results = []

    for description in descriptions:
        result = classify_product(description, categories)
        results.append(result)
        print(f"Description: {description} \n -> Classified as: {result}\n")

    return results


if __name__ == "__main__":




    # Example list of product descriptions
    product_descriptions = [
        "A smartphone with 128GB storage and 6GB RAM.",
        "A comfortable cotton t-shirt, available in various colors.",
        "A blender with 3-speed settings and a glass jar.",
    ]

    # Example categories
    categories = ["Electronics", "Clothing", "Home Appliances", "Sports Equipment", "Toys"]

    # Classify each product
    classified_results = classify_products(product_descriptions, categories)

    # Output the results
    for i, category in enumerate(classified_results):
        print(f"Product {i + 1}: {category}")
