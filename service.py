import sys
import os

from flask import Flask, request, session, render_template

app = Flask(__name__)
app_root = app.root_path
app.config['DEBUG'] = False

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/homepage.html')
def homepage():
    return render_template('homepage.html')

@app.route('/news.html')
def news():
    return render_template('news.html')

@app.route('/participate.html')
def participate():
    return render_template('participate.html')

@app.route('/programs.html')
def programs():
    return render_template('programs.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/about_campus.html')
def about_campus():
    return render_template('about_campus.html')

@app.route('/about_company.html')
def about_company():
    return render_template('about_company.html')

@app.route('/about_people.html')
def about_people():
    return render_template('about_people.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)