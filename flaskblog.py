from flask import Flask, escape, request

# Tells Flask where to look for templates and static files
app = Flask(__name__)

# Forward slash is just the root/home page of the website
@app.route('/')
def hello():
    return "<h1>Hello Home</h1>"

# Use the below command as a workaround to get the terminal to run the flask site
# set FLASK_DEBUG=1 && python -m flask run