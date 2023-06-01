#!/usr/bin/env python3
"""
Module containing class SeesionAuth
inheriting from Auth and implementing
Session Authentication
"""
from api.v1.auth.auth import Auth
from typing import Optional
from uuid import uuid4


class SessionAuth(Auth):
    """
    Contains Session Authentication
    implementation
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> Optional[str]:
        """
        Creates a Session ID for a user_id
        """
        if not user_id or type(user_id) != str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
