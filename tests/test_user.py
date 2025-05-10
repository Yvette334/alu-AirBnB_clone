#!/usr/bin/python3
"""Unittest for User model"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for the User class"""

    def setUp(self):
        self.user = User()

    def test_instance(self):
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))


if __name__ == '__main__':
    unittest.main()
