#!/usr/bin/python3
"""
--------------------------------------------------------
This module define the user_statu class for each user
--------------------------------------------------------
"""


from models.base_model import BaseModel


class UserStatus(BaseModel):
    """
    ------------------------------------------------
    UserStatus Class
    - Attributes:
        -- id, status_value
    - Methods:
        --
    ------------------------------------------------
    """

    status_value: str = ""
