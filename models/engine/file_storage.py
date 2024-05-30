#!/usr/bin/python3
"""a class that serializes instances to a JSON file
and deserializes JSON file to instances"""

import json
import os


class FileStorage:
    """initializing class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary_objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj_dict = {
                key: obj.to_dict()
                for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = globals().get(class_name)
                    if cls:
                        FileStorage.__objects[key] = cls(**value)
