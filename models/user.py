from database import obter_conexao
from flask_login import UserMixin

class User(UserMixin):
    id: str
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    @classmethod
    def get(cls, id):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        SELECT = 'SELECT * FROM tb_usuarios WHERE usu_id=?'
        cursor.execute(SELECT, (id,))
        dados = cursor.fetchone()
        if dados:
            user = User(dados[1],dados[2], dados[3])
            user.id = dados[0]
        else: 
            user = None
        return user
    
    @classmethod
    def select_user_by_email(cls, email):
        conexao = obter_conexao()
        cursor = conexao.cursor()
        SELECT = 'SELECT * FROM tb_usuarios WHERE usu_email=?'
        cursor.execute(SELECT, (email,))
        dados = cursor.fetchone()
    
        if dados:
            user = User(dados['usu_nome'], dados['usu_email'], dados['usu_senha'])
            user.id = dados['usu_id']

            conexao.close()
            return user
        
        return None
    
    @classmethod
    def insert_user(cls, nome, email, senha):
        conexao = obter_conexao()

        cursor = conexao.cursor()
        INSERT = 'INSERT INTO tb_usuarios(usu_nome, usu_email, usu_senha) VALUES (?, ?, ?)'
        cursor.execute(INSERT, (nome, email, senha,))
        conexao.commit()

        cursor.close()
        conexao.close()


    