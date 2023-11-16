from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    list_options = [{"name": "Bug Fix",
              "path": "bug_fix.txt"},
             {"name": "Feature Change",
              "path": "feature_change.txt"}]

    return render_template('index.html', options = list_options)

@app.route("/receive_id")
def test():
    pass

if __name__ == "__main__":
    app.run(debug=True)
