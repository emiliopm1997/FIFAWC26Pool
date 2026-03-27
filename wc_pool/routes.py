from flask import jsonify


def apply_route(app):

    @app.route("/", methods=["GET"])
    def test():
        return jsonify({"message": "API is working"})
