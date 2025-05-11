#!/usr/bin/python3
"""
Unit tests for console.py
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
import os


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test cases"""
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def setUp(self):
        """Reset storage before each test"""
        storage.all().clear()
        storage.save()

    def test_quit(self):
        """Test quit command"""
        with self.assertRaises(SystemExit):
            self.console.do_quit("")

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.do_EOF(""))
            self.assertEqual(f.getvalue(), "\n")

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.emptyline()
            self.assertEqual(f.getvalue(), "")

    def test_create_missing_class(self):
        """Test create command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_create("")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_create_invalid_class(self):
        """Test create command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_create("InvalidClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_create_valid_class(self):
        """Test create command with valid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_create("BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)  # UUID length

    def test_show_missing_class(self):
        """Test show command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show("")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_show_invalid_class(self):
        """Test show command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show("InvalidClass 123")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show_missing_id(self):
        """Test show command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show("BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_show_no_instance(self):
        """Test show command with non-existent instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_show("BaseModel 123")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_destroy_missing_class(self):
        """Test destroy command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy("")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy("InvalidClass 123")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_destroy_missing_id(self):
        """Test destroy command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy("BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_destroy_no_instance(self):
        """Test destroy command with non-existent instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_destroy("BaseModel 123")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_all_no_class(self):
        """Test all command with no class specified"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_all("")
            self.assertEqual(f.getvalue(), "[]\n")

    def test_all_invalid_class(self):
        """Test all command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_all("InvalidClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_update_missing_class(self):
        """Test update command with missing class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_update("")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_update_invalid_class(self):
        """Test update command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_update("InvalidClass 123")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_update_missing_id(self):
        """Test update command with missing id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_update("BaseModel")
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_update_no_instance(self):
        """Test update command with non-existent instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_update("BaseModel 123")
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_count_no_class(self):
        """Test count command with no class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_count("")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_count_invalid_class(self):
        """Test count command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_count("InvalidClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_count_valid_class(self):
        """Test count command with valid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_create("BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_count("BaseModel")
            self.assertEqual(f.getvalue(), "1\n")

    def test_default_invalid_syntax(self):
        """Test default method with invalid syntax"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.default("invalid.syntax")
            self.assertTrue("Unknown syntax" in f.getvalue())

    def test_default_all(self):
        """Test default method with all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.default("BaseModel.all()")
            self.assertEqual(f.getvalue(), "[]\n")

    def test_default_count(self):
        """Test default method with count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.default("BaseModel.count()")
            self.assertEqual(f.getvalue(), "0\n")


if __name__ == '__main__':
    unittest.main()
