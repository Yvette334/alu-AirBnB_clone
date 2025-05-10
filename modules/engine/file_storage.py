#!/usr/bin/python3
import json
""" this is a class that defines file storage"""
from models.base_model import BaseModel


class FileStorage:
    """ class that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ a public instance method all that returns the dictionary
        object(private)
        """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        ob = str(obj.__class__.__name__)
        FileStorage.__objects[f"{ob}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        objdic = {}
        for k, v in FileStorage.__objects.items():
            objdic[k] = v.to_dict()

        with open(FileStorage.__file_path, mode='w') as file:
            json.dump(objdic, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path) as file:
                FileStorage.__objects = json.load(file)
                for k, v in FileStorage.__objects.items():
                    class_name = v["__class__"]
                    del v["__class__"]
                    self.new(eval(class_name)(**v))
        except FileNotFoundError:
            pass
