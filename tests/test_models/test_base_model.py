#!/usr/bin/python3
"""
Unit tests for the BaseModel class
"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
import os
import json
import models


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up test cases"""
        self.model = BaseModel()
        self.model.name = "Test Model"
        self.model.my_number = 89

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """Test initialization of BaseModel"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test string representation of BaseModel"""
        string = str(self.model)
        self.assertIn("[BaseModel]", string)
        self.assertIn("id", string)
        self.assertIn("created_at", string)
        self.assertIn("updated_at", string)
        self.assertIn("name", string)
        self.assertIn("my_number", string)

    def test_save(self):
        """Test save method of BaseModel"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict method of BaseModel"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["name"], "Test Model")
        self.assertEqual(model_dict["my_number"], 89)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_init_from_dict(self):
        """Test initialization from dictionary"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)
        self.assertEqual(new_model.name, "Test Model")
        self.assertEqual(new_model.my_number, 89)
        self.assertIsNot(new_model, self.model)


if __name__ == "__main__":
    unittest.main()
