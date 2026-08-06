from flask import render_template
from config import Config


def register_routes(app):

    @app.route("/")
    def home():

        app.logger.info("Homepage accessed")

        platform = {

            "status": "Operational",

            "uptime": "99.98%",

            "environment": Config.FLASK_ENV.capitalize(),

            "cloud": "Microsoft Azure",

            "services": "6 / 6",

            "security_status": "Protected",

            "critical_vulnerabilities": "0",

            "high_vulnerabilities": "0",

            "secret_scanning": "Enabled",

            "audit": "Passed",

            "iac": "Terraform",

            "region": Config.AZURE_REGION,

            "drift": "None",

            "alerts": "0",

            "response_time": "142 ms",

            "incident": "None in 30d",

            "version": Config.APP_VERSION,

            "application_name": Config.APP_NAME

        }

        return render_template(
            "index.html",
            platform=platform
        )



    @app.route("/health")
    def health():

        app.logger.info("Health endpoint accessed")

        return {

            "status": "healthy",

            "application": Config.APP_NAME,

            "version": Config.APP_VERSION

        }



    @app.route("/metrics")
    def metrics():

        app.logger.info("Metrics endpoint accessed")

        return {

            "application": Config.APP_NAME,

            "version": Config.APP_VERSION,

            "environment": Config.FLASK_ENV,

            "status": "Operational",

            "cloud": "Microsoft Azure",

            "iac": "Terraform",

            "region": Config.AZURE_REGION,

            "pipeline": "GitHub Actions"

        }