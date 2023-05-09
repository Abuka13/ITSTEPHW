from flask import Flask

app = Flask(__name__)

#flask --app main run
#http://127.0.0.1:5000
@app.route("/")
def home():
    return "<p>Hello, World!</p>"
@app.route('/index')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'