#!/usr/bin/python3
"""
Test module for BaseModel class
"""
import unittest
import os
import json
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test cases"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except:
            pass


class TestBaseModel_Save(unittest.TestCase):
    """Test cases for BaseModel save method"""

    def setUp(self):
        """Set up test cases"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_save_once(self):
        """test if when saved once the date is diff"""
        Bm1 = BaseModel()
        first_update = Bm1.updated_at
        Bm1.save()
        self.assertLess(first_update, Bm1.updated_at)

    def test_save_twice(self):
        """test if when saved twice the date is diff"""
        Bm1 = BaseModel()
        first_update = Bm1.updated_at
        Bm1.save()
        second_update = Bm1.updated_at
        Bm1.save()
        self.assertLess(second_update, Bm1.updated_at)


# Add more test classes as needed

if __name__ == "__main__":
    unittest.main()
