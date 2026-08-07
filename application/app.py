from flask import Flask
import logging

from config import Config
from routes import register_routes


def create_app():
    """
    Application Factory.
    Creates and configures the Flask application.
    """

    app = Flask(__name__)

    logging.basicConfig(
        level=Config.LOG_LEVEL,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    register_routes(app)

    return app


app = create_app()


if __name__ == "__main__":

    app.logger.info(f"Starting {Config.APP_NAME}")

    app.run(
        host="0.0.0.0",
        port=Config.PORT,
        debug=Config.FLASK_ENV == "development"
    )
