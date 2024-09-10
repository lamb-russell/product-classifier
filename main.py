import csv
import pandas as pd
from typing import List
from classify import classify_product

def load_product_data(product_file: str) -> pd.DataFrame:
    """
    Load product data from a CSV file.
    Args:
        product_file (str): Path to the product CSV file.
    Returns:
        pd.DataFrame: A pandas DataFrame containing product_id and description.
    """
    try:
        return pd.read_csv(product_file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise

def load_category_data(category_file: str) -> List[str]:
    """
    Load category data from a CSV file.
    Args:
        category_file (str): Path to the category CSV file.
    Returns:
        List[str]: A list of categories.
    """
    try:
        df = pd.read_csv(category_file)
        return df['category'].tolist()  # Assuming the CSV has a column 'category'
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise

def predict_category(description: str, categories: List[str]) -> str:
    """
    Classify the product description.
    Args:
        description (str): Product description to classify.
        categories (List[str]): List of categories.
    Returns:
        str: The predicted category.
    """
    predicted_category = classify_product(description, categories)
    return predicted_category

def process_product_classification(product_file: str, category_file: str, output_file: str) -> None:
    """
    Process the product classification and add categories to the product CSV file.
    Args:
        product_file (str): Path to the input CSV containing product descriptions.
        category_file (str): Path to the input CSV containing categories.
        output_file (str): Path to the output CSV file where results will be saved.
    """
    # Load product and category data
    products = load_product_data(product_file)
    categories = load_category_data(category_file)

    # Initialize columns for predicted category
    products['predicted_category'] = ''

    # Iterate through the products and classify each one
    for index, row in products.iterrows():
        description = row['description']
        predicted_category = predict_category(description, categories)
        products.at[index, 'predicted_category'] = predicted_category

    # Save the updated dataframe with predicted category to a new CSV
    products.to_csv(output_file, index=False)
    print(f"Classification results saved to {output_file}")

if __name__ == "__main__":
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser(description='Classify products and add predicted categories to a CSV file.')
    parser.add_argument('product_file', type=str, help='Path to the CSV file containing product descriptions.')
    parser.add_argument('category_file', type=str, help='Path to the CSV file containing categories.')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file to save the results.')

    # Parse command-line arguments
    args = parser.parse_args()

    # Call the classification processing function
    process_product_classification(args.product_file, args.category_file, args.output_file)
