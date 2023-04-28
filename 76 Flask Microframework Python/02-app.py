from flask import Flask

app = Flask(__name__)
#flask run
@app.route("/")
def hello_world():
    return "<p>Hello, World!!</p>"
