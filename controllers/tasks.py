from flask import Flask, render_template, url_for, request, Blueprint, redirect
from models.task import Task
from flask_login import login_required, current_user

bp = Blueprint("tasks", __name__, url_prefix="/tasks")

@bp.route('/', methods = ["POST", "GET"])
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
        
        tarefas = Task.filter_all(id, descricao, status, prazo, prioridade, categoria, criacao)
        
        return render_template("tasks/inicial.html", tarefas = tarefas)

    tarefas =  Task.select_all(current_user.id)
    return render_template("tasks/inicial.html", tarefas = tarefas)

@bp.route('/<int:id>/remove', methods=['POST'])
@login_required
def remove(id):
    Task.delete_tarefa(id)
    return redirect(url_for("tasks.inicial"))

@bp.route('/criar', methods =["POST", "GET"])
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
        Task.insert_tarefa(nome, descricao, status, prazo, prioridade, categoria, id)
        return redirect(url_for("tasks.inicial"))


    return render_template("tasks/tarefas.html")

@bp.route('/editar', methods = ["POST", "GET"])
@login_required
def editar():
    tarefas =  Task.select_all(current_user.id)

    if request.method == "POST":
        id = request.form["id"]
        descricao = request.form["descricao"]
        status = request.form["status"]
        prioridade = request.form["prioridade"]
        prazo = request.form["prazo"]
        categoria = request.form["categoria"]

        Task.update_all(id, descricao, status, prazo, prioridade, categoria)

        return redirect(url_for("tasks.inicial"))
        


    return render_template("tasks/editar.html", tarefas = tarefas)