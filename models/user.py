from database.init_db import session
from database.init_db import User as usuario
from flask_login import UserMixin

class User(UserMixin):
    id: str
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    @classmethod
    def get(cls, id):
<<<<<<< Updated upstream
        conexao = obter_conexao()
        cursor = conexao.cursor()
        SELECT = 'SELECT * FROM tb_usuarios WHERE usu_id=%s'
        cursor.execute(SELECT, (id,))
        dados = cursor.fetchone()
=======
        dados = session.query(usuario).where(usuario.id == id).scalar()
        
>>>>>>> Stashed changes
        if dados:
            user = User(dados.nome,dados.email, dados.senha)
            user.id = dados.id
        else: 
            user = None
        return user
    
    @classmethod
    def select_user_by_email(cls, email):
<<<<<<< Updated upstream
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        SELECT = 'SELECT * FROM tb_usuarios WHERE usu_email=%s'
        cursor.execute(SELECT, (email,))
        dados = cursor.fetchone()
    
=======
        dados = session.query(usuario).where(usuario.email == email).first()
        
>>>>>>> Stashed changes
        if dados:
            user = User(dados.nome, dados.email, dados.senha)
            user.id = dados.id
            return user
        
        return None
    
    @classmethod
    def insert_user(cls, nome, email, senha):
<<<<<<< Updated upstream
        conexao = obter_conexao()

        cursor = conexao.cursor(dictionary=True)
        INSERT = 'INSERT INTO tb_usuarios (usu_nome, usu_email, usu_senha) VALUES (%s, %s, %s)'
        cursor.execute(INSERT, (nome, email, senha,))
        conexao.commit()

        cursor.close()
        conexao.close()
=======
        user = usuario(nome = nome, email = email, senha = senha)
        session.add(user)
>>>>>>> Stashed changes


    