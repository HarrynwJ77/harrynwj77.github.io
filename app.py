from flask import Flask, request, render_template, jsonify
import os
from flask_cors import CORS

TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')

# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
CORS(app)

@app.route("/", methods=['POST', 'GET'])
def home():
    list_options = [{"name": "Bug Fix",
              "path": "bug_fix"},
             {"name": "Feature Change",
              "path": "feature_change"}]

    return render_template('index.html', options = list_options)

@app.route("/receive_request", methods=['POST', 'GET'])
def bug_fix():
    data = request.form.get('name')
    print(data)
    return "cool"


if __name__ == "__main__":
    app.run(debug=True)
