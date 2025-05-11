#!/usr/bin/python3
"""
Test module for City class
"""
import os
import sys
import unittest

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, parent_dir)

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_city_inherits_from_base_model(self):
        """Test that City inherits from BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes(self):
        """Test that City has the correct attributes"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attributes_are_strings(self):
        """Test that City attributes are strings"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)


if __name__ == "__main__":
    unittest.main()
