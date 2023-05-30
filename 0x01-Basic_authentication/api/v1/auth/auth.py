#!/usr/bin/env python3
"""
Module that creates a class to manage
API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Class template for the authentication
    system
    """
    def require_auth(self, path: str, excluded_path: List[str]) -> bool:
        """
        Returns False if path is in excluded_path
        """

        if path is None:
            return True
        if excluded_path is None or len(excluded_path) == 0:
            return True
        if path:
            print(path)
            if path in excluded_path or path + '/' in excluded_path:
                return False
            else:
                return True

    def authorization_header(self, request=None) -> str:
        """
        Returns None or str accrding to request
        """
        if not request:
            return None
        authorization = request.headers.get('Authorization')
        print("authorization is {}".format(authorization))
        if authorization:
            return authorization
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None or User according to request
        """
        return None
