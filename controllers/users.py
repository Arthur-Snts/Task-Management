from flask import render_template, Blueprint, url_for, request, flash, redirect
from models.user import User
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        user = User.select_user_by_email(email)

        if user:
            hash = user.senha
        else:
            return render_template('users/index.html', frase = "Email Inexistente, Tente novamente, ou se Cadastre")
        
        if user and check_password_hash(hash, senha):
            
            login_user(user)

            return redirect(url_for('tasks.inicial'))
    return render_template('users/index.html', frase = None)

@bp.route('/cadastro', methods = ["POST", "GET"])
def cadastro():

    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        nome = request.form["nome"]
        hash = generate_password_hash(senha)

        User.insert_user(nome, email, hash)
        user = User.select_user_by_email(email)
        
        login_user(user)
        return redirect(url_for("tasks.inicial"))
    
    return render_template('users/cadastro.html')

@bp.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect(url_for("users.login"))