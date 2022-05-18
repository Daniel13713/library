#!/usr/bin/python3
"""
--------------------------------------------------------
This module define the user class for user and admin
--------------------------------------------------------
"""


from models.base_model import BaseModel
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class Loan(BaseModel):
    """
    ------------------------------------------------
    User Class
    - Attributes:
        -- id, loan_date, return_date
        -- book_id, user_id
    - Methods:
        --
    ------------------------------------------------
    """

    loan_date: datetime = datetime.utcnow()
    return_date: datetime = datetime.utcnow()
