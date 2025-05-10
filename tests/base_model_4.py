#!/usr/bin/env python3
from models.base_model import BaseModel

model = BaseModel()
s = str(model)
assert "[BaseModel]" in s and model.id in s
print("OK")
