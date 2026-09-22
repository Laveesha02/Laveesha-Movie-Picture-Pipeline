from flask import Flask
from flask_cors import CORS

from movies.movies_api import movies_api


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(movies_api, url_prefix="/api")

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
