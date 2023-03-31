import os
import uuid
import json
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

def get_user(username):
    return User.query.filter_by(username=username).first()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = get_user(username)
        if user:
            user = User(user.id, user.username, user.password)
            login_user(user)
            return redirect(url_for('index'))
        else:
            return "Invalid username", 401
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    print(f"Current user: {current_user.username}")
    return render_template('index.html')

def add_user(username, password):
    user_id = str(uuid.uuid4())
    new_user = User(id=user_id, username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
