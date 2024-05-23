from flask import render_template
from app import app

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/home')
def home():
    user={'username': 'Duc'}
    return render_template('home.html', title='Home', user=user)