#!/usr/bin/env python3
"""
Main file
"""
from models.user import User

print(User.__tablename__)

for column in User.__table__.columns:
    print(f"{column.name}: {column.type}")

