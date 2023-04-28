from flask import Flask, request

app = Flask(__name__)
# flask run


@app.route("/")
def hello_world():
    app.logger.debug("Mensaje a nivel Debug")
    app.logger.info(f"Entramos al path {request.path}")
    app.logger.warn("Mensaje a nivel Warnnig")
    app.logger.error("Mensaje a nivel Error")
    return "<p>Hello, World!!</p>"
