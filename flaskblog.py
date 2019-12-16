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
        'title': 'Neurons',
        'sub_title': 'The Building Blocks of a neural network',
        'content': '"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."',
        'date_posted': '16 December, 2019',
        'image': 'neuron-image.jpeg',
        'image-name': 'Neuron'
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

@app.route('/neural_networks')
def neural_networks():
    return render_template('neural_networks.html', title='Neural Networks', posts=posts)

@app.route('/neurons')
def neurons():
    return render_template('neural_networks_posts/neurons.html', title='Neurons')







