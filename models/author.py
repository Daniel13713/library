#!/usr/bin/python3
"""
--------------------------------------------------------
This module define the user class for user and admin
--------------------------------------------------------
"""


from models.base_model import BaseModel
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class Author(BaseModel):
    """
    ------------------------------------------------
    User Class
    - Attributes:
        -- id, first_name, last_name
    - Methods:
        --
    ------------------------------------------------
    """

    first_name: str = ""
    last_name: str = ""
