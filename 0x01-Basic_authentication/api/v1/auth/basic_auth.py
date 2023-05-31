#!/usr/bin/env python3
"""
Module containing class BasicAuth
inheriting from Auth and implementing
BasicAuth for REST API
"""
from api.v1.auth.auth import Auth
from typing import Optional, Tuple
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> Optional[str]:
        """
        Returns decoded value of Base64 string of
        base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
        except Exception as e:
            return None
        return decoded.decode(encoding='utf-8')

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header:
            str) -> Tuple[Optional[str], Optional[str]]:
        """
        Returns user email and password from Base64 decoded value
        (decoded_base64_authorization_header)
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_cred = decoded_base64_authorization_header.split(':')
        return user_cred[0], user_cred[1]
