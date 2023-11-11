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
        self.__objects = obj

    def save(self):
        # serializes __objects to the JSON file (path: __file_path)
        json.dump(self.__objects, self.__file_path)

    def reload(self):
        # deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        # otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as file:
                self.__objects = json.load(file)
