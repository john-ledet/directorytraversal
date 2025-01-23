from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath("base_folder")

@app.route("/")
def index():
    return "Welcome! Try /view?file=public_file.txt"

@app.route("/view", methods=["GET"])
def view_file():
    file_name = request.args.get("file")
    if not file_name:
        return "Please provide a file parameter, e.g. /view?file=public_file.txt"
    requested_path = os.path.join(BASE_DIR, file_name)
    requested_path = os.path.abspath(requested_path)

    # serve file if check passes
    if os.path.isfile(requested_path):
        return send_file(requested_path)
    else:
        abort(404, "File not found.")

if __name__ == "__main__":
    app.run(debug=True)