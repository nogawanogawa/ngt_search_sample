import os
from search import DocSimilarity
from flask import Flask, request

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    model = DocSimilarity()

    @app.route('/search')
    def search():
        word_1 = request.args.get('word_1')
        word_2 = request.args.get('word_2')
        res = model.search([word_1, word_2])
        return jsonify(res)

    return app