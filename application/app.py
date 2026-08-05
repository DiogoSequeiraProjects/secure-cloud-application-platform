
from flask import Flask, render_template
import logging

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/")
def home():

    app.logger.info("Homepage accessed")

    platform = {

        "status": "Operational",

        "uptime": "99.98%",

        "environment": "Production",

        "cloud": "Microsoft Azure",

        "services": "6 / 6",

        "security_status": "Protected",

        "critical_vulnerabilities": "0",

        "high_vulnerabilities": "0",

        "secret_scanning": "Enabled",

        "audit": "Passed",

        "iac": "Terraform",

        "region": "West Europe",

        "drift": "None",

        "alerts": "0",

        "response_time": "142 ms",

        "incident": "None in 30d"

    }

    return render_template(
        "index.html",
        platform=platform
    )

@app.route("/metrics")
def metrics():

    return {

        "application": "Secure Cloud Platform",

        "version": "1.0.0",

        "environment": "Production",

        "cloud": "Azure",

        "iac": "Terraform",

        "pipeline": "GitHub Actions",

        "status": "Operational"

    }

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "Secure Cloud Platform"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

