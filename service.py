import sys
import os

from flask import Flask, request, session, render_template

app = Flask(__name__)
app_root = app.root_path
app.config['DEBUG'] = False

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/participate')
def participate():
    return render_template('participate.html')

@app.route('/programs')
def programs():
	return render_template('programs.html')

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')