from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/blog')
def blog():
    return render_template('homepage.html')