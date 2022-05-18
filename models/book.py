#!/usr/bin/python3
"""
--------------------------------------------------------
This module define the book class for all Library'sbooks
--------------------------------------------------------
"""

import uuid
from models.base_model import BaseModel


class Book(BaseModel):
    """
    ------------------------------------------------
    Books Class
    - Attributes:
        -- id, code(PK, str), title, publication,
        -- copies, editorial, catgory
    - Methods:
        --
    ------------------------------------------------
    """

    code: str = str(uuid.uuid4())  # temporal PK
    title: str = ""
    publication_date: int = ""  # Only year
    copies: int = 0
    editorial: str = ""
    category_id: int = 0  # FK
