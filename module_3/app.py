## This is the entry point for the Flask application.
## It initializes the Flask app and runs it on the specified host and port.

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
