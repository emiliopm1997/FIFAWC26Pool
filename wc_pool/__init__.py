import os
from flask import Flask
from .routes import register_routes
from .utils.logger import Logger

logger = Logger().get_logger()


def _is_main_process() -> bool:
        """
        Determine if the current process is the main Flask runtime process.

        Returns
        -------
        bool
            True if running in the Flask reloader's child process,
            False otherwise.
        """
        return os.environ.get("WERKZEUG_RUN_MAIN") == "true"

def start_pool() -> Flask:
    """Create and configure the Flask application instance.

    Returns
    -------
    Flask
        Configured Flask application instance.
    """
    app = Flask(__name__)

    if _is_main_process():
        logger.info(
            "\n{}\n{} FIFA WC 2026 Pool {}".format(
                "#" * 80, "-" * 30, "-" * 30
            )
        )
        logger.info("Starting API ...")
        register_routes(app)
        logger.info("Ready to receive requests ...")
    else:
        register_routes(app)

    return app
