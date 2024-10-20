from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from models import User
from werkzeug.security import generate_password_hash, check_password_hash


login_manager = LoginManager()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPERMEGADIFICIL'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)





@app.route('/', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        user = User.select_user_by_email(email) 
        
        hash = user.senha
        if user and check_password_hash(hash, senha):
            login_user(user)

            return redirect(url_for('inicial'))
    return render_template('index.html')

@app.route('/cadastro', methods = ["POST", "GET"])
def cadastro():

    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        nome = request.form["nome"]
        hash = generate_password_hash(senha)

        User.insert_user(nome, email, hash)
        user = User.select_user_by_email(email)
        login_user(user)
        return redirect(url_for("inicial"))
    
    return render_template('cadastro.html')



@app.route('/inicial', methods = ["POST", "GET"])
@login_required
def inicial():
    
    if request.method =="POST":
        descricao = request.form["descricao"]
        status = request.form["status"]
        prioridade = request.form["prioridade"]
        prazo = request.form["prazo"]
        categoria = request.form["categoria"]
        criacao = request.form["criacao"]
        id = current_user.id
        
        tarefas = User.filter_all(id, descricao, status, prazo, prioridade, categoria, criacao)
        
        return render_template("inicial.html", tarefas = tarefas)

    tarefas =  User.select_all(current_user.id)
    return render_template("inicial.html", tarefas = tarefas)

@app.route('/<int:id>/remove', methods=['POST'])
@login_required
def remove(id):
    User.delete_tarefa(id)
    return redirect(url_for("inicial"))



@app.route('/criar', methods =["POST", "GET"])
@login_required
def criar():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        status = request.form["status"]
        prioridade = request.form["prioridade"]
        prazo = request.form["prazo"]
        categoria = request.form["categoria"]
        id = current_user.id
        User.insert_tarefa(nome, descricao, status, prazo, prioridade, categoria, id)
        return redirect(url_for("inicial"))


    return render_template("tarefas.html")


@app.route('/editar', methods = ["POST", "GET"])
@login_required
def editar():
    tarefas =  User.select_all(current_user.id)

    if request.method == "POST":
        id = request.form["id"]
        descricao = request.form["descricao"]
        status = request.form["status"]
        prioridade = request.form["prioridade"]
        prazo = request.form["prazo"]
        categoria = request.form["categoria"]

        User.update_all(id, descricao, status, prazo, prioridade, categoria)

        return redirect("inicial")
        


    return render_template("editar.html", tarefas = tarefas)



@app.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect(url_for("login"))