from database import obter_conexao
from database.init_db import session
from database.init_db import Task as tarefa

class Task():
    id: str
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    @classmethod
    def filter_all(cls, id, desc, status, prazo, prioridade, categoria, criacao):
        conexao = obter_conexao()
<<<<<<< Updated upstream
        cursor = conexao.cursor(dictionary=True)
        SELECT = "SELECT * FROM tb_tarefas WHERE"
=======
        cursor = conexao.cursor()
        SELECT = "SELECT * FROM tb_tasks WHERE"
>>>>>>> Stashed changes
        variaveis = []


        if desc:
            if len(variaveis) > 0:
                SELECT += " and"
<<<<<<< Updated upstream
            SELECT += " tar_descricao like %s"
=======
            SELECT += " descricao like ?"
>>>>>>> Stashed changes
            variaveis.append('%' + desc + '%')
        if status:
            if len(variaveis) > 0:
                SELECT += " and"
<<<<<<< Updated upstream
            SELECT += " tar_status =  %s"
=======
            SELECT += " status =  ?"
>>>>>>> Stashed changes
            variaveis.append(status)
        if prazo:
            if len(variaveis) > 0:
                SELECT += " and"
<<<<<<< Updated upstream
            SELECT += " tar_prazo between curdate() and %s or tar_prazo between %s and curdate()"
=======
            SELECT += " prazo between curdate() and ? or prazo between ? and curdate()"
>>>>>>> Stashed changes
            variaveis.append(prazo)
            variaveis.append(prazo)
        if prioridade:
            if len(variaveis) > 0:
                SELECT += " and"
<<<<<<< Updated upstream
            SELECT += " tar_prioridade = %s"
=======
            SELECT += " prioridade = ?"
>>>>>>> Stashed changes
            variaveis.append(prioridade)
        if categoria:
            if len(variaveis) > 0:
                SELECT += " and"
<<<<<<< Updated upstream
            SELECT += " tar_categoria = %s"
=======
            SELECT += " categoria = ?"
>>>>>>> Stashed changes
            variaveis.append(categoria)
        if criacao:
            if len(variaveis) > 0:
                SELECT += " and"
<<<<<<< Updated upstream
            SELECT += " tar_data_criacao between %s and curdate() + interval 1 day"
=======
            SELECT += " data_de_criacao between ? and curdate() + interval 1 day"
>>>>>>> Stashed changes
            variaveis.append(criacao)



<<<<<<< Updated upstream
        SELECT += " and tar_usuario_id = %s "
        if len(variaveis) == 0:
            SELECT = "SELECT * FROM tb_tarefas WHERE tar_usuario_id = %s"
=======
        SELECT += " and us_id = ? "
        if len(variaveis) == 0:
            SELECT = "SELECT * FROM tb_tasks WHERE us_id = ?"
>>>>>>> Stashed changes
        variaveis.append(id)
        tuple(variaveis)

        cursor.execute(SELECT, variaveis)
        tarefas = cursor.fetchall()
        conexao.commit()

        cursor.close()
        conexao.close()

        return tarefas
    
    @classmethod
    def select_all(cls, id):
        conexao = obter_conexao()
<<<<<<< Updated upstream
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_tarefas WHERE tar_usuario_id = %s'
=======
        cursor = conexao.cursor()
        SELECT = 'SELECT * FROM tb_tasks WHERE usu_id = ?'
>>>>>>> Stashed changes
        cursor.execute(SELECT, (id,))
        tarefas = cursor.fetchall()

        cursor.close()
        conexao.close()
        
        return tarefas
    
    @classmethod
    def delete_tarefa(cls, id):
        conexao = obter_conexao()
<<<<<<< Updated upstream
        cursor = conexao.cursor(dictionary=True)
        DELETE = 'DELETE FROM tb_tarefas WHERE tar_id = %s'
=======
        cursor = conexao.cursor()
        DELETE = 'DELETE FROM tb_tasks WHERE id = ?'
>>>>>>> Stashed changes
        cursor.execute(DELETE, (id,))
        conexao.commit()

        cursor.close()
        conexao.close()

    @classmethod
    def insert_tarefa(cls, nome,  desc, status, limite, prioridade, categoria, id):
        conexao = obter_conexao()
<<<<<<< Updated upstream
        cursor = conexao.cursor(dictionary=True)
        INSERT = 'INSERT INTO tb_tarefas (tar_nome, tar_descricao, tar_status, tar_prazo, tar_prioridade, tar_categoria, tar_usuario_id) VALUES (%s, %s, %s, %s, %s, %s, %s)'
=======
        cursor = conexao.cursor()
        INSERT = 'INSERT INTO tb_tasks (nome, descricao, status, prazo, prioridade, categoria, us_id) VALUES (?, ?, ?, ?, ?, ?, ?)'
>>>>>>> Stashed changes
        cursor.execute(INSERT, (nome, desc, status, limite, prioridade, categoria, id))
        conexao.commit()

        cursor.close()
        conexao.close()

    @classmethod
    def update_all(cls, id,  desc, status, limite, prioridade, categoria):
        conexao = obter_conexao()
<<<<<<< Updated upstream
        cursor = conexao.cursor(dictionary=True)
        UPDATE = "UPDATE tb_tarefas SET"
=======
        cursor = conexao.cursor()
        UPDATE = "UPDATE tb_tasks SET"
>>>>>>> Stashed changes
        variaveis = []

        if desc:
            if len(variaveis) > 0:
                UPDATE += " ,"
<<<<<<< Updated upstream
            UPDATE += " tar_descricao = %s"
=======
            UPDATE += " descricao = ?"
>>>>>>> Stashed changes
            variaveis.append(desc)
        if status:
            if len(variaveis) > 0:
                UPDATE += " ,"
<<<<<<< Updated upstream
            UPDATE += " tar_status = %s"
=======
            UPDATE += " status = ?"
>>>>>>> Stashed changes
            variaveis.append(status)
        if limite:
            if len(variaveis) > 0:
                UPDATE += " ,"
<<<<<<< Updated upstream
            UPDATE += " tar_prazo = %s"
=======
            UPDATE += " prazo = ?"
>>>>>>> Stashed changes
            variaveis.append(limite)
        if prioridade:
            if len(variaveis) > 0:
                UPDATE += " ,"
<<<<<<< Updated upstream
            UPDATE += " tar_prioridade = %s"
=======
            UPDATE += " prioridade = ?"
>>>>>>> Stashed changes
            variaveis.append(prioridade)
        if categoria:
            if len(variaveis) > 0:
                UPDATE += " ,"
<<<<<<< Updated upstream
            UPDATE += " tar_categoria = %s"
            variaveis.append(categoria)
        UPDATE += "WHERE tar_id = %s "
=======
            UPDATE += " categoria = ?"
            variaveis.append(categoria)
        UPDATE += "WHERE id = ? "
>>>>>>> Stashed changes

        variaveis.append(id)
        tuple(variaveis)

        if len(variaveis) > 1:
            cursor.execute(UPDATE, variaveis)
        conexao.commit()

        cursor.close()
        conexao.close()