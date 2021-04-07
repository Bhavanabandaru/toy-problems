from flask import Flask
app = Flask(__name__)
  
@app.route('/')
def index():
    return '<h1>Hello</h1>'

@app.route("/bhavana")
def bhavana():
   return "Hello, Bhavana!!"
