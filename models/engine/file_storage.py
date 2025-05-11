#!/usr/bin/python3
"""
Module for FileStorage class
"""
import datetime
import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        serialized = {}
        for key, obj in self.__objects.items():
            serialized[key] = obj.to_dict()
        
        with open(self.__file_path, 'w') as f:
            json.dump(serialized, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        Only if the JSON file exists; otherwise, do nothing
        No exception should be raised if the file doesn't exist
        """
