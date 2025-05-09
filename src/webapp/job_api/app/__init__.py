from flask import Flask
from .routes import init_routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    # Đăng ký routes
    init_routes(app)
    
    return app