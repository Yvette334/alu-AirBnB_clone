#!/usr/bin/python3
"""
Unit tests for the Place class
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
import os


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up test cases"""
        self.place = Place()
        self.place.city_id = "city-123"
        self.place.user_id = "user-123"
        self.place.name = "Cozy Apartment"
        self.place.description = "A beautiful apartment in the city center"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 37.7749
        self.place.longitude = -122.4194
        self.place.amenity_ids = ["amenity-1", "amenity-2"]

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        """Test initialization of Place"""
        self.assertIsInstance(self.place, Place)
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))

    def test_attributes(self):
        """Test Place attributes"""
        self.assertEqual(self.place.city_id, "city-123")
        self.assertEqual(self.place.user_id, "user-123")
        self.assertEqual(self.place.name, "Cozy Apartment")
        self.assertEqual(self.place.description, "A beautiful apartment in the city center")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)
        self.assertEqual(self.place.amenity_ids, ["amenity-1", "amenity-2"])

    def test_str(self):
        """Test string representation of Place"""
        string = str(self.place)
        self.assertIn("[Place]", string)
        self.assertIn("id", string)
        self.assertIn("city_id", string)
        self.assertIn("user_id", string)
        self.assertIn("name", string)
        self.assertIn("description", string)

    def test_to_dict(self):
        """Test to_dict method of Place"""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["city_id"], "city-123")
        self.assertEqual(place_dict["user_id"], "user-123")
        self.assertEqual(place_dict["name"], "Cozy Apartment")
        self.assertEqual(place_dict["description"], "A beautiful apartment in the city center")
        self.assertEqual(place_dict["number_rooms"], 2)
        self.assertEqual(place_dict["number_bathrooms"], 1)
        self.assertEqual(place_dict["max_guest"], 4)
        self.assertEqual(place_dict["price_by_night"], 100)
        self.assertEqual(place_dict["latitude"], 37.7749)
        self.assertEqual(place_dict["longitude"], -122.4194)
        self.assertEqual(place_dict["amenity_ids"], ["amenity-1", "amenity-2"])


if __name__ == "__main__":
    unittest.main()
