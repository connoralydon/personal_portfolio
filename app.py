from flask import Flask
from markupsafe import escape
# to escape variables when returning html

app = Flask(__name__)

name = "Connor Lydon"

# use this current directory for the files in the app
@app.route("/name") # different URL routes
def title_func():
	return f"<p>Welcome to {escape(name)}'s website!<p>"

# @gfg_decorator
# def hello_decorator():
#     print("Gfg")
# these are the same
# def hello_decorator():
#     print("Gfg")
    
# hello_decorator = gfg_decorator(hello_decorator)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

# using flask -debug run # to allow live updates on server

