import os


class Config:

    APP_NAME = os.getenv(
        "APP_NAME",
        "Secure Cloud Platform"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )

    FLASK_ENV = os.getenv(
        "FLASK_ENV",
        "development"
    )

    PORT = int(
        os.getenv(
            "FLASK_PORT",
            "5000"
        )
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    AZURE_REGION = os.getenv(
        "AZURE_REGION",
        "West Europe"
    )