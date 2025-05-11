#!/usr/bin/python3
"""
Unit tests for the User class
"""
import unittest
from models.user import User
from models.base_model import BaseModel
import os


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up test cases"""
        self.user = User()
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "Test"
        self.user.last_name = "User"

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """Test initialization of User"""
        self.assertIsInstance(self.user, User)
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attributes(self):
        """Test User attributes"""
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")

    def test_str(self):
        """Test string representation of User"""
        string = str(self.user)
        self.assertIn("[User]", string)
        self.assertIn("id", string)
        self.assertIn("email", string)
        self.assertIn("password", string)
        self.assertIn("first_name", string)
        self.assertIn("last_name", string)

    def test_to_dict(self):
        """Test to_dict method of User"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "password123")
        self.assertEqual(user_dict["first_name"], "Test")
        self.assertEqual(user_dict["last_name"], "User")


if __name__ == "__main__":
    unittest.main()
