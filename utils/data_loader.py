# The data_loader.py will load and handle test data from external sources (e.g., JSON, CSV). In this case, we are using a JSON file to load car models and price ranges.

import json
import os

class DataLoader:
    def __init__(self, data_file='resources/test_data.json'):
        self.data_file = data_file
        self.data = None
        self.load_data()

    def load_data(self):
        """Loads data from the specified JSON file."""
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Data file {self.data_file} not found!")

        with open(self.data_file, 'r') as file:
            self.data = json.load(file)

    def get_car_models(self):
        """Returns a list of car models from the loaded data."""
        return self.data.get('car_models', [])

    def get_price_ranges(self):
        """Returns a list of price ranges from the loaded data."""
        return self.data.get('price_ranges', [])

    def get_test_data(self, key):
        """Returns specific data by key."""
        return self.data.get(key, None)
