#!/usr/bin/python3
"""
--------------------------------------------------------
This module define the user class for user and admin
--------------------------------------------------------
"""


from models.base_model import BaseModel
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class User(BaseModel):
    """
    ------------------------------------------------
    User Class
    - Attributes:
        -- id, first_name, last_name, age,
        -- email, phoneNumber, joined_date
        -- user_status_id
    - Methods:
        --
    ------------------------------------------------
    """

    first_name: str = ""
    last_name: str = ""
    age: int = 0
    email: str = ""
    phoneNumber: str = ""
    joined_date: datetime = datetime.utcnow()
    user_status_id: int = 0  # FK
