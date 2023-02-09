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