"""
Encryptor

https://github.com/rafaeelaudibert/Encryptor/
"""

import os

import sentry_sdk
import werkzeug
from dotenv import load_dotenv
from flask import Flask
from flask import jsonify
from flask import request
from sentry_sdk.integrations.flask import FlaskIntegration

from .encryptors import *

# Configure dotenv
load_dotenv()

# Sentry initialization, if possible
if os.environ.get("SENTRY_DSN", None) or os.getenv("SENTRY_DSN"):
    sentry_sdk.init(
        dsn=os.environ.get("SENTRY_DSN", None) or os.getenv("SENTRY_DSN"),
        release="encryptor@{}".format(
            os.environ.get("PACKAGE_VERSION", None) or os.getenv("PACKAGE_VERSION")
        )
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
    # pylint: disable=unused-variable
    @app.route("/api/ceasar/encrypt/<text>")
    def ceasar_encrypt(text):
        offset = request.args.get("offset", Ceasar.DEFAULT_OFFSET)

        return jsonify({"status": 200, "content": Ceasar.encrypt(text, offset)})

    @app.route("/api/ceasar/decrypt/<text>")
    def ceasar_decrypt(text):
        offset = request.args.get("offset", Ceasar.DEFAULT_OFFSET)

        return jsonify({"status": 200, "content": Ceasar.decrypt(text, offset)})

    @app.route("/api/vigenere/encrypt/<text>")
    def vigenere_encrypt(text):
        tabula_recta = request.args.get("tabula_recta", Vigenere.ALPHABET)
        key = request.args.get("key", Vigenere.KEY)

        return jsonify(
            {"status": 200, "content": Vigenere.encrypt(text, key, tabula_recta)}
        )

    @app.route("/api/vigenere/decrypt/<text>")
    def vigenere_decrypt(text):
        tabula_recta = request.args.get("tabula_recta", Vigenere.ALPHABET)
        key = request.args.get("key", Vigenere.KEY)

        return jsonify(
            {"status": 200, "content": Vigenere.decrypt(text, key, tabula_recta)}
        )

    @app.route("/api/railfence/encrypt/<text>")
    def railfence_encrypt(text):
        rail_height = request.args.get("rail_height", RailFence.DEFAULT_RAILS)

        return jsonify({"status": 200, "content": RailFence.encrypt(text, rail_height)})

    @app.route("/api/railfence/decrypt/<text>")
    def railfence_decrypt(text):
        rail_height = request.args.get("rail_height", RailFence.DEFAULT_RAILS)

        return jsonify({"status": 200, "content": RailFence.decrypt(text, rail_height)})

    @app.route("/api/blowfish/encrypt/<text>")
    def blowfish_encrypt(text):
        mode = request.args.get("mode", Blowfish.DEFAULT_MODE)
        return jsonify({"status": 200, "content": Blowfish.encrypt(text, mode)})

    @app.route("/api/blowfish/decrypt/<text>")
    def blowfish_decrypt(text):
        mode = request.args.get("mode", Blowfish.DEFAULT_MODE)

        return jsonify({"status": 200, "content": Blowfish.decrypt(text, mode)})

    @app.route("/api/rsa/encrypt/<text>")
    def rsa_encrypt(text):
        input_n = request.args.get("n", Rsa.DEFAULT_N)
        input_e = request.args.get("e", Rsa.DEFAULT_E)

        return jsonify({"status": 200, "content": Rsa.encrypt(text, input_n, input_e)})

    @app.route("/api/rsa/decrypt/<text>")
    def rsa_decrypt(text):
        input_p = request.args.get("p", Rsa.DEFAULT_P)
        input_q = request.args.get("q", Rsa.DEFAULT_Q)
        input_e = request.args.get("e", Rsa.DEFAULT_E)

        return jsonify(
            {"status": 200, "content": Rsa.decrypt(text, input_p, input_q, input_e)}
        )

    @app.route("/api/error")
    def trigger_error():
        return jsonify({"status": 200, "content": "1 / 0 = {}".format(1 / 0)})

    # ERROR HANDLERS
    def handle_errors(err):
        return jsonify(
            {"status": err.code, "error": err.name, "content": err.description}
        )

    app.register_error_handler(400, handle_errors)
    app.register_error_handler(500, handle_errors)

    return app
