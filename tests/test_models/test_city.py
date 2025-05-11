#!/usr/bin/python3
"""
Simple test script for City class
"""
import os
import sys

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, parent_dir)

from models.city import City

# Create a City instance
city = City()

# Check if it has the required attributes
if hasattr(city, "state_id") and hasattr(city, "name"):
    if isinstance(city.state_id, str) and isinstance(city.name, str):
        if city.state_id == "" and city.name == "":
            print("OK")
        else:
            print("Attributes not initialized as empty strings")
    else:
        print("Attributes are not strings")
else:
    print("Missing required attributes")
