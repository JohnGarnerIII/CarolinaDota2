# pip install flask
from flask import Flask

# Make sure  to download python-dotenv
# pip install python-dotenv
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

@app.route("/")
def home(): 
    return "<h1>Hello, World!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)