import os

import sentry_sdk
import werkzeug
from dotenv import load_dotenv
from flask import Flask
from flask import jsonify
from flask import request
from sentry_sdk.integrations.flask import FlaskIntegration

from encryptor.encryptors import *

# Configure dotenv
load_dotenv()

# Sentry initialization, if possible
if os.environ.get("SENTRY_DSN", None) or os.getenv("SENTRY_DSN"):
    sentry_sdk.init(
        dsn=os.environ.get("SENTRY_DSN", None) or os.getenv("SENTRY_DSN"),
        release="encryptor@{}".format(os.environ.get("PACKAGE_VERSION", None)
                                      or os.getenv("PACKAGE_VERSION"))
        or "encryptor@no_version",
        integrations=[FlaskIntegration()],
    )


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "encryptor.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # ROUTES
    @app.route("/api/ceasar/encrypt/<text>")
    def ceasar_encrypt(text):
        offset = request.args.get("offset", Ceasar.DEFAULT_OFFSET)

        return jsonify({
            "status": 200,
            "content": Ceasar.encrypt(text, offset)
        })

    @app.route("/api/ceasar/decrypt/<text>")
    def ceasar_decrypt(text):
        offset = request.args.get("offset", Ceasar.DEFAULT_OFFSET)

        return jsonify({
            "status": 200,
            "content": Ceasar.decrypt(text, offset)
        })

    @app.route("/api/railfence/encrypt/<text>")
    def railfence_encrypt(text):
        rail_height = request.args.get("rail_height", RailFence.DEFAULT_RAILS)

        return jsonify({
            "status": 200,
            "content": RailFence.encrypt(text, rail_height)
        })

    @app.route("/api/railfence/decrypt/<text>")
    def railfence_decrypt(text):
        rail_height = request.args.get("rail_height", RailFence.DEFAULT_RAILS)

        return jsonify({
            "status": 200,
            "content": RailFence.decrypt(text, rail_height)
        })

    @app.route("/api/error")
    def trigger_error():
        return jsonify({"status": 200, "content": "1 / 0 = {}".format(1 / 0)})

    # ERROR HANDLERS
    def handle_errors(e):
        return jsonify({
            "status": e.code,
            "error": e.name,
            "content": e.description
        })

    app.register_error_handler(400, handle_errors)
    app.register_error_handler(500, handle_errors)

    return app
