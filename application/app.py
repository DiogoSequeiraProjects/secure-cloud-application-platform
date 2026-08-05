
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
    return render_template("index.html")


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "Secure Cloud Platform"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)