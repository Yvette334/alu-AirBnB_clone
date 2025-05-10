#!/usr/bin/env python3
from models.base_model import BaseModel
model = BaseModel()
assert isinstance(model.id, str)
print("OK")
