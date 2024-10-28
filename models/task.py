from database import obter_conexao

class Task():
    id: str
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

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
    def insert_tarefa(cls, nome,  desc, status, limite, prioridade, categoria, id):
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        INSERT = 'INSERT INTO tb_tarefas (tar_nome, tar_descricao, tar_status, tar_prazo, tar_prioridade, tar_categoria, tar_usuario_id) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(INSERT, (nome, desc, status, limite, prioridade, categoria, id))
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