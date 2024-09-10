# Product Classifier Project

This project provides a tool for classifying product descriptions into predefined categories using the `OllamaLLM` model from `LangChain`. It supports both individual and batch classification, with logging enabled for tracking model responses and outputs. Additionally, the project includes unit tests for validating the classification functionality.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Setup Instructions](#setup-instructions)
3. [Usage](#usage)
   - [Classify a Single Product](#classify-a-single-product)
   - [Classify Multiple Products](#classify-multiple-products)
   - [Process Product CSV File](#process-product-csv-file)
4. [Testing](#testing)
5. [Logging](#logging)

---

## Project Structure

The project files are organized as follows:

```
product_classifier/
│
├── classify.py         # Main script for classifying product descriptions
├── main.py             # Script to process products from a CSV file and save results
├── test.py             # Unit tests for the classification functions
├── README.md           # Project documentation (this file)
├── .gitignore          # Ignore common unwanted files and directories in git
```

---

## Setup Instructions

### Prerequisites

- **Python 3.10+**: Ensure you have Python 3.10 or a later version installed.
- **Virtual Environment**: It's recommended to use a virtual environment for managing dependencies.

### Steps to Set Up the Environment

1. **Clone the Repository** (if applicable):

   ```bash
   git clone <repository_url>
   cd product_classifier
   ```

2. **Set Up a Virtual Environment**:

   If a virtual environment is not set up, create one:

   ```bash
   python3 -m venv .venv
   ```

3. **Activate the Virtual Environment**:

   - On macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

4. **Install the Required Dependencies**:

   Install the required libraries, including `langchain` and `OllamaLLM`:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Classify a Single Product

To classify a single product into predefined categories, use the `classify_product` function from `classify.py`:

```python
from classify import classify_product

description = "A smartphone with 128GB storage and 6GB RAM."
categories = ["Electronics", "Clothing", "Home Appliances"]

result = classify_product(description, categories)
print(f"Classified Category: {result}")
```

### Classify Multiple Products

To classify a list of products, use the `classify_products` function:

```python
from classify import classify_products

descriptions = [
    "A smartphone with 128GB storage and 6GB RAM.",
    "A comfortable cotton t-shirt, available in various colors.",
    "A blender with 3-speed settings and a glass jar."
]
categories = ["Electronics", "Clothing", "Home Appliances", "Sports Equipment", "Toys"]

results = classify_products(descriptions, categories)
for i, result in enumerate(results):
    print(f"Product {i + 1}: {result}")
```

### Process Product CSV File

The `main.py` script allows you to classify product descriptions from a CSV file and save the results to a new CSV file. The input CSV should contain a `description` column, and the category CSV should list the available categories in a `category` column.

Example usage:

```bash
python main.py product_file.csv category_file.csv output_file.csv
```

This will classify all products in `product_file.csv` and store the results, including a `predicted_category` column, in `output_file.csv`.

---

## Testing

Unit tests for the classification functions are available in `test.py`. The tests can be run using the `unittest` module:

```bash
python -m unittest test.py
```

This will validate the `classify_product` and `classify_products` functions against predefined test cases.
