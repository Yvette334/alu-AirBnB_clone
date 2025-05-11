#!/usr/bin/python3
"""Defines unittests user file"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_init_with_kwargs(self):
        user_dict = {
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**user_dict)
        self.assertEqual(user.email, user_dict['email'])
        self.assertEqual(user.password, user_dict['password'])
        self.assertEqual(user.first_name, user_dict['first_name'])
        self.assertEqual(user.last_name, user_dict['last_name'])
