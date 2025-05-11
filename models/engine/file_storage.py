#!/usr/bin/python3
"""
Module for FileStorage class
"""
import datetime
import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes back to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        json_objects = {}
        for key, obj in self.__objects.items():
            json_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }

        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, 'r') as f:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        class_name = value["__class__"]
                        if class_name in classes:
                            self.__objects[key] = classes[class_name](**value)
        except Exception:
            pass
