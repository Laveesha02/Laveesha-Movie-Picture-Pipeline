from flask import jsonify


def get_movies():
    return jsonify({
        "movies": []
    })
