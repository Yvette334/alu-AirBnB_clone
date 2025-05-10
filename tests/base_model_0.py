#!/usr/bin/env python3
from models.base_model import BaseModel
import time

model = BaseModel()
prev = model.updated_at
time.sleep(0.01)
model.save()
assert model.updated_at > prev
print("OK")
print("Test started")
