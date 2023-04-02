from flask import Flask

app = Flask(__name__)
#http://127.0.0.1:5000
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"