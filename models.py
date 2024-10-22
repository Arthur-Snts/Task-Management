from flask_login import UserMixin
import mysql.connector as sql

def obter_conexao():
    db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_gerenciamento'
    }
    conn = sql.connect(**db_config, auth_plugin='mysql_native_password')
    
    return conn

class User(UserMixin):
    id: str
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Inserir funções de controle de login

    @classmethod
    def get(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        SELECT = 'SELECT * FROM tb_usuarios WHERE usu_id=%s'
        cursor.execute(SELECT, (id,))
        dados = cursor.fetchone()
        if dados:
            user = User(dados[1],dados[2], dados[3])
            user.id = dados[0]
        else: 
            user = None
        return user

    
# SELECIONAR USER POR ID   
    @classmethod
    def select_user_by_email(cls, email):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_usuarios WHERE usu_email=%s'
        cursor.execute(SELECT, (email,))
        dados = cursor.fetchone()
    
        if dados:
            user = User(dados['usu_nome'], dados['usu_email'], dados['usu_senha'])
            user.id = dados['usu_id']

            conexao.close()
        
        return user

# FUNÇÕES INSERT
    @classmethod
    def insert_user(cls, nome, email, senha):
        conexao = obter_conexao()

        cursor = conexao.cursor(dictionary=True)
        INSERT = 'INSERT INTO tb_usuarios (usu_nome, usu_email, usu_senha) VALUES (%s, %s, %s)'
        cursor.execute(INSERT, (nome, email, senha,))
        conexao.commit()

        cursor.close()
        conexao.close()

    @classmethod
    def insert_tarefa(cls, nome,  desc, status, limite, prioridade, categoria, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        INSERT = 'INSERT INTO tb_tarefas (tar_nome, tar_descricao, tar_status, tar_prazo, tar_prioridade, tar_categoria, tar_usuario_id) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(INSERT, (nome, desc, status, limite, prioridade, categoria, id))
        conexao.commit()

        cursor.close()
        conexao.close()

# FUNÇÕES UPDATE  
    @classmethod
    def update_tarefa_desc(cls, desc, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        UPDATE = 'UPDATE tb_tarefas SET tar_descricao = %s WHERE tar_id = %s'
        cursor.execute(UPDATE, (desc, id,))
        conexao.commit()

        cursor.close()
        conexao.close()
    
    @classmethod
    def update_tarefa_status(cls, status, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        UPDATE = 'UPDATE tb_tarefas SET tar_status = %s WHERE tar_id = %s'
        cursor.execute(UPDATE, (status, id,))
        conexao.commit()

        cursor.close()
        conexao.close()
    
    @classmethod
    def update_tarefa_prazo(cls, prazo, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        UPDATE = 'UPDATE tb_tarefas SET tar_prazo = %s WHERE tar_id = %s'
        cursor.execute(UPDATE, (prazo, id,))
        conexao.commit()

        cursor.close()
        conexao.close()

    @classmethod
    def update_all(cls, id,  desc, status, limite, prioridade, categoria):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        UPDATE = "UPDATE tb_tarefas SET"
        variaveis = []

        if desc:
            if len(variaveis) > 0:
                UPDATE += " ,"
            UPDATE += " tar_descricao = %s"
            variaveis.append(desc)
        if status:
            if len(variaveis) > 0:
                UPDATE += " ,"
            UPDATE += " tar_status = %s"
            variaveis.append(status)
        if limite:
            if len(variaveis) > 0:
                UPDATE += " ,"
            UPDATE += " tar_prazo = %s"
            variaveis.append(limite)
        if prioridade:
            if len(variaveis) > 0:
                UPDATE += " ,"
            UPDATE += " tar_prioridade = %s"
            variaveis.append(prioridade)
        if categoria:
            if len(variaveis) > 0:
                UPDATE += " ,"
            UPDATE += " tar_categoria = %s"
            variaveis.append(categoria)
        UPDATE += "WHERE tar_id = %s "

        variaveis.append(id)
        tuple(variaveis)

        if len(variaveis) > 1:
            cursor.execute(UPDATE, variaveis)
        conexao.commit()

        cursor.close()
        conexao.close()

    @classmethod
    def filter_all(cls, id, desc, status, prazo, prioridade, categoria, criacao):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = "SELECT * FROM tb_tarefas WHERE"
        variaveis = []


        if desc:
            if len(variaveis) > 0:
                SELECT += " and"
            SELECT += " tar_descricao like %s"
            variaveis.append('%' + desc + '%')
        if status:
            if len(variaveis) > 0:
                SELECT += " and"
            SELECT += " tar_status =  %s"
            variaveis.append(status)
        if prazo:
            if len(variaveis) > 0:
                SELECT += " and"
            SELECT += " tar_prazo between curdate() and %s or tar_prazo between %s and curdate()"
            variaveis.append(prazo)
            variaveis.append(prazo)
        if prioridade:
            if len(variaveis) > 0:
                SELECT += " and"
            SELECT += " tar_prioridade = %s"
            variaveis.append(prioridade)
        if categoria:
            if len(variaveis) > 0:
                SELECT += " and"
            SELECT += " tar_categoria = %s"
            variaveis.append(categoria)
        if criacao:
            if len(variaveis) > 0:
                SELECT += " and"
            SELECT += " tar_data_criacao between %s and curdate() + interval 1 day"
            variaveis.append(criacao)



        SELECT += " and tar_usuario_id = %s "
        if len(variaveis) == 0:
            SELECT = "SELECT * FROM tb_tarefas WHERE tar_usuario_id = %s"
        variaveis.append(id)
        tuple(variaveis)

        cursor.execute(SELECT, variaveis)
        tarefas = cursor.fetchall()
        conexao.commit()

        cursor.close()
        conexao.close()

        return tarefas
        
        


# FUNÇÃO DELETE
    @classmethod
    def delete_tarefa(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        DELETE = 'DELETE FROM tb_tarefas WHERE tar_id = %s'
        cursor.execute(DELETE, (id,))
        conexao.commit()

        cursor.close()
        conexao.close()


    @classmethod
    def select_all(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_tarefas WHERE tar_usuario_id = %s'
        cursor.execute(SELECT, (id,))
        tarefas = cursor.fetchall()

        cursor.close()
        conexao.close()
        
        return tarefas

# FUNÇÕES SELECT (FILTROS)
    @classmethod
    def select_by_status(cls, status, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_tarefas WHERE tar_status = %s and tar_usuario_id = %s'
        cursor.execute(SELECT, (status, id))
        tarefas = cursor.fetchall()

        cursor.close()
        conexao.close()
        
        return tarefas
    
    @classmethod
    def select_by_create(cls, create, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_tarefas WHERE tar_data_criacao = %s and tar_usuario_id = %s'
        cursor.execute(SELECT, (create, id))
        tarefas = cursor.fetchall()

        cursor.close()
        conexao.close()
        
        return tarefas
    
    @classmethod
    def select_by_prazo(cls, prazo, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_tarefas WHERE tar_prazo = %s and tar_usuario_id = %s'
        cursor.execute(SELECT, (prazo, id))
        tarefas = cursor.fetchall()

        cursor.close()
        conexao.close()
        
        return tarefas

    @classmethod
    def select_by_prioridade(cls, prioridade, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_tarefas WHERE tar_prioridade = %s and tar_usuario_id = %s'
        cursor.execute(SELECT, (prioridade, id))
        tarefas = cursor.fetchall()

        cursor.close()
        conexao.close()
        
        return tarefas
    
    @classmethod
    def select_by_keyword(cls, keyword, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_tarefas WHERE tar_descricao LIKE %s and tar_usuario_id = %s'
        cursor.execute(SELECT, ('%' + keyword + '%', id))
        tarefas = cursor.fetchall()

        cursor.close()
        conexao.close()
        
        return tarefas
    
    @classmethod
    def select_by_categoria(cls, categoria, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_tarefas WHERE tar_categoria = %s and tar_usuario_id = %s'
        cursor.execute(SELECT, (categoria, id))
        tarefas = cursor.fetchall()

        cursor.close()
        conexao.close()
        
        return tarefas
