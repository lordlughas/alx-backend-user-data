#1/usr/bin/env python3
"""
API authentication module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
    """ check done to know if API requires authenticationi"""
    if path is None or not exluded_paths:
        return True
    for item in exluded_paths:
        if item.endswith('*') and path.startswith(item[:-1]):
            return False
    return True

def authorization_header(self, request=None) -> str:
    """ Checks if Authorization request header is present
        & contains values """
    if request is None or "Authorization" not in request.headers:
            return None
        else:
            return request.headers.get('Authorization')

def current_user(self, request=None) -> TypeVar('User'):
        """ placeholder """
        return None
