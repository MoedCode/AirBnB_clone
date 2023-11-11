#!/usr/bin/python3
import json
import os.path


class FileStorage:
    __file_path: str = "file.json"
    __objects: dict = {}

    def __init__(self):
        pass

    def all(self):
        # returns the dictionary __objects
        return self.__objects

    def new(self, obj):
        # sets in __objects the obj with key <obj class name>.id
        # self.__objects = obj
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        # serializes __objects to the JSON file (path: __file_path)

        with open(self.__file_path, "w") as file:
            serialized_objects = {}
            for key, value in self.__objects.items():
                serialized_objects[key] = value.to_dict()

            json.dump(serialized_objects, file)

    def reload2(self):
        # deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        # otherwise, do nothing. If the file doesn’t exist, no exception should be raised)

        if os.path.exists(self.__file_path) and os.stat(self.__file_path).st_size > 0:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                dictionary = json.loads(file.read())
                for value in dictionary.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
