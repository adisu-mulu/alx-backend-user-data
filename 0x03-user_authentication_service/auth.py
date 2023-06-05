#!/usr/bin/env python3
"""
Contains authentication methods for
users
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """
    Takes in a string (password) argument and
    returns bytes which are salted hash of input
    """
    pass_bytes = password.encode()
    hash_passwd = bcrypt.hashpw(pass_bytes, bcrypt.gensalt())
    return hash_passwd


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        Initialize authentication instances
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a user if it does not exist, hashes the password
        saves the user then returns the user. If user already exists
        raise a ValueError
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(user.email))
        except (InvalidRequestError, NoResultFound):
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user