#!/usr/bin/python3
"""init magic method for models directory"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
