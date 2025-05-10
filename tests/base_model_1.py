#!/usr/bin/env python3
from models.base_model import BaseModel

model = BaseModel()
d = model.to_dict()
assert type(d["created_at"]) is str
assert d["__class__"] == "BaseModel"
print("OK")
