## This is the routes.py file for the Flask application.
## It defines the routes for the application and handles requests to the root URL.  

from flask import Blueprint, render_template
from .db import get_analysis_results

main = Blueprint('main', __name__)

@main.route("/")
def index():
    results = get_analysis_results()
    return render_template("index.html", results=results)
