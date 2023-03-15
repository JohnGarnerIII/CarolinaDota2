# pip install flask
# pip install python-dotenv
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home(): 
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
