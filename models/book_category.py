#!/usr/bin/python3
"""
--------------------------------------------------------
This module define the category class for each book
--------------------------------------------------------
"""


from models.base_model import BaseModel
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BookCategory(BaseModel):
    """
    ------------------------------------------------
    BookCategory Class
    - Attributes:
        -- id, category_name
    - Methods:
        --
    ------------------------------------------------
    """

    category_name: str = ""
