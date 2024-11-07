from flask import Flask, redirect, url_for
from flask_login import LoginManager
from models.models import User
from controllers import users, tasks

login_manager = LoginManager()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPERMEGADIFICIL'
login_manager.init_app(app)

app.register_blueprint(users.bp)
app.register_blueprint(tasks.bp)



@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return redirect(url_for("users.login"))


