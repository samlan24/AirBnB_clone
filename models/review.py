#!/usr/bin/python3
"""a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class initialization"""

    place_id = ""
    user_id = ""
    text = ""
