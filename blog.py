from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template(
            'home.html',
            title='My Home Page',
            mouseover='1 smart developer in your area <!> <!> <!> Click now!'
            )