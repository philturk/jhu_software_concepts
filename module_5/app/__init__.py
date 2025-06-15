"""
This is the __init__.py file for the Flask application.
It sets up the application factory pattern for creating a Flask app instance.
"""

from flask import Flask
from .routes import main

def create_app():
    """Application factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.register_blueprint(main)
    return app
