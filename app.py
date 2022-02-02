from flask import Flask, jsonify
from flask import render_template


app = Flask(__name__)


@app.route("/ping")
def index():
    return render_template('index.html')


if __name__ == "__main__": 
	app.run(debug = True, port=8000)