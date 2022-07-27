import flask


def create_app():
    app = flask.Flask(__name__)

    with app.app_context():
        return app