import os

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

from constants import DATA_DIR
from utils import do_query


app = Flask(__name__)


@app.route("/perform_query", methods=["POST"])
def perform_query():
    data = request.json
    file_name = data["file_name"]
    if not os.path.exists(os.path.join(DATA_DIR, file_name)):
        raise BadRequest

    return jsonify(do_query(data))


if __name__ == "__main__":
    app.run()
