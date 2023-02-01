from flask import Flask, jsonify
from app import routes, models
import os

app = Flask(__name__)


# @app.route('/')
# def index():
#     return jsonify({"Vishal": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
