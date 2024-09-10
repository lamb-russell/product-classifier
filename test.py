import unittest
from typing import List
from classify import classify_product, classify_products


class TestProductClassifier(unittest.TestCase):

    def test_classify_product(self):
        description = "A smartphone with 128GB storage and 6GB RAM."
        categories = ["Electronics", "Clothing", "Home Appliances"]

        # Call the function and assert the response
        result = classify_product(description, categories)

        # Check that the result is one of the categories
        self.assertIn(result, categories)

        print(f"Test classify_product result: {result}")

    def test_classify_products(self):
        descriptions = [
            "A smartphone with 128GB storage and 6GB RAM.",
            "A comfortable cotton t-shirt, available in various colors.",
            "A blender with 3-speed settings and a glass jar."
        ]
        categories = ["Electronics", "Clothing", "Home Appliances", "Sports Equipment", "Toys"]

        # Call the classify_products function
        results = classify_products(descriptions, categories)

        # Verify the results are within the provided categories
        for result in results:
            self.assertIn(result, categories)

        print(f"Test classify_products results: {results}")
        self.assertEqual(results,['Electronics', 'Clothing', 'Home Appliances'])


if __name__ == "__main__":
    unittest.main()
