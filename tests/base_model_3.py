#!/usr/bin/env python3
from models.base_model import BaseModel

model = BaseModel()
assert hasattr(model, "created_at")
print("OK")
