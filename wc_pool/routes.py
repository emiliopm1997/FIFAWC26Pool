from flask import Flask, jsonify
from wc_pool.utils.logger import Logger

# logger = Logger().get_logger()


def register_routes(app: Flask):
    """
    Register all API routes with the Flask application.

    This function centralizes route definitions and attaches them to the
    provided Flask app instance. It allows for modular expansion of routes
    as the project grows.

    Parameters
    ----------
    app : Flask
        The Flask application instance to which routes will be registered.
    """

    @app.route("/", methods=["GET"])
    def test():
        """
        Health check endpoint.

        This endpoint verifies that the API is running and reachable.

        Returns
        -------
        Response
            JSON response containing a status message.
        """
        # logger.info("Test log...")
        print("test")
        return jsonify({"message": "API is working"})
