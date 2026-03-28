from flask import Flask
from wc_pool.routes import register_routes


def start_pool() -> Flask:
    """Create and configure the Flask application instance.

    Returns
    -------
    Flask
        Configured Flask application instance.
    """
    app = Flask(__name__)

    register_routes(app)

    return app
