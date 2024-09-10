# Product Categorizer Project

This project implements a product classification tool using the `OllamaLLM` model from `LangChain`. The tool classifies product descriptions into a set of predefined categories based on natural language processing.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Setup Instructions](#setup-instructions)
3. [Usage](#usage)
   - [Classify a Single Product](#classify-a-single-product)
   - [Classify Multiple Products](#classify-multiple-products)
4. [Testing](#testing)
5. [Logging](#logging)

---

## Project Structure

The project is structured as follows:

```
product_categorizer/
│
├── classify.py         # Main script containing the classification logic
├── test.py             # Unit tests for the classification functions
├── code.txt            # (Reserved for future use or custom scripts)
├── .venv/              # Virtual environment setup
│   ├── pyvenv.cfg      # Configuration file for the virtual environment
│   ├── .gitignore      # Ignoring virtual environment files
└── README.md           # This readme file
```

---

## Setup Instructions

### Prerequisites

1. **Python 3.10+**: Ensure Python 3.10 or higher is installed on your machine.
2. **Virtual Environment**: The project uses a virtual environment to manage dependencies. The virtual environment is created using `virtualenv`.

### Steps to Set Up the Environment

1. **Clone the Repository** (if applicable):

   ```bash
   git clone <repository_url>
   cd product_categorizer
   ```

2. **Set Up Virtual Environment**:

   If a virtual environment does not exist, create one:

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

4. **Install Required Dependencies**:

   After activating the environment, install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have installed the necessary `langchain` libraries and `OllamaLLM` support for the model.

---

## Usage

The `classify.py` script provides functions to classify a product description into predefined categories.

### Classify a Single Product

To classify a single product, use the `classify_product` function. Here’s an example:

```python
from classify import classify_product

description = "A smartphone with 128GB storage and 6GB RAM."
categories = ["Electronics", "Clothing", "Home Appliances"]

result = classify_product(description, categories)
print(f"Classified Category: {result}")
```

### Classify Multiple Products

To classify multiple products in one go, use the `classify_products` function:

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

---

## Testing

Unit tests for the classification functions are provided in `test.py`. The `unittest` framework is used for testing.

### Running the Tests

To run the tests, use the following command:

```bash
python -m unittest test.py
```

This will test both the `classify_product` and `classify_products` functions with predefined test cases.

---

## Logging

The `classify.py` script has logging enabled to track important information during execution. The logging setup is as follows:

- **Logging Level**: `INFO` (can be changed to `DEBUG` for more verbosity).
- **Format**: The log messages include the timestamp, logger name, log level, and message.

Example log entries:

```
2024-09-09 14:33:23,847 - __main__ - INFO - A smartphone with 128GB storage and 6GB RAM.
2024-09-09 14:33:23,847 - __main__ - INFO - Electronics, Clothing, Home Appliances
2024-09-09 14:33:23,847 - __main__ - INFO - Electronics
```

The logger will capture:
- Product descriptions being classified.
- Categories provided to the model.
- The result returned by the model.

---

## Additional Notes

- The `OllamaLLM` model will be called during runtime, so ensure the model is properly configured and accessible in your environment.
- Performance may vary based on the response time of the model and the complexity of the product descriptions.

---

This README provides an overview of the project, including setup, usage, and testing. If you encounter any issues or need further assistance, please feel free to reach out.