#!/usr/bin/python3
"""" doc """
from models.engine.file_storage import FileStorage

storage = FileStorage()
print(storage.all())
storage.reload()
