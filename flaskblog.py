from flask import Flask, escape, request
# Use the below command as a workaround to get the terminal to run the flask site
# set FLASK_DEBUG=1 && python -m flask run
# Below can be used if you are running the flaskblog module with python locally
# if __name__ == '__main__':
#     app.run(debug=True)
# Tells Flask where to look for templates and static files
app = Flask(__name__)


# Forward slash is just the root/home page of the website
@app.route('/')
@app.route('/home')
def home():
    return "<h1>Hello Rory</h1>"


@app.route('/about')
def about():
    return "<h1>About Page</h1>"



