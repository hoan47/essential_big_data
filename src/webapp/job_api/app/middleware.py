from flask import request, abort
from functools import wraps
from config import Config

def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key and api_key == Config.API_KEY:
            return f(*args, **kwargs)
        else:
            abort(401, description="Invalid or missing API Key")
    return decorated