#!/usr/bin/env python3
"""
Module containing class BasicAuth
inheriting from Auth and implementing
BasicAuth for REST API
"""
from api.v1.auth.auth import Auth
from typing import Optional


class BasicAuth(Auth):
    """
    Contains BasicAuth implementation
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> Optional[str]:
        """
        Returns the Base64 part of authorization header
        for Basic authentication
        """
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        auth_list = authorization_header.split(" ")
        if auth_list[0] != 'Basic':
            return None
        else:
            return auth_list[1]
