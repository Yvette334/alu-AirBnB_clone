#!/usr/bin/python3
"""
Unit tests for the console (command interpreter)
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for the HBNB command interpreter"""

    def setUp(self):
        """Set up test cases"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue()
            self.assertIn("Documented commands", output)

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)
            # Check if the output is a valid UUID
            try:
                uuid.UUID(output)
                is_valid_uuid = True
            except ValueError:
                is_valid_uuid = False
            self.assertTrue(is_valid_uuid)

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue()
            self.assertIn(obj_id, output)
            self.assertIn("BaseModel", output)

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {obj_id}")
        
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue()
            self.assertIn("** no instance found **", output)

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
        
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue()
            self.assertIn("BaseModel", output)

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'update BaseModel {obj_id} name "Test Name"')
        
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue()
            self.assertIn("Test Name", output)


if __name__ == "__main__":
    unittest.main()
