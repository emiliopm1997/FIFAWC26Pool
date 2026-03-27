from flask import Flask
from wc_pool.routes import apply_route


def start_pool():
    app = Flask(__name__)

    apply_route(app)

    return app
