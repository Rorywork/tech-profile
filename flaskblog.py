from flask import Flask, escape, request, render_template
# Use the below command as a workaround to get the terminal to run the flask site
# set FLASK_DEBUG=1 && python -m flask run
# Below can be used if you are running the flaskblog module with python locally
# if __name__ == '__main__':
#     app.run(debug=True)
# Tells Flask where to look for templates and static files
app = Flask(__name__)

posts = [
    {
        'author': 'Rory Lindsay',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2019'
    },
    {
        'author': 'Ciara Lindsay',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 23, 2019'
    }
]       



# Forward slash is just the root/home page of the website
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')



