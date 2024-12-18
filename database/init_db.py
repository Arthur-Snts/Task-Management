<<<<<<< Updated upstream
# Importando o conector MySQL
import mysql.connector

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': ''
}

try:
    # Tentando estabelecer uma conexão
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("Conexão estabelecida com sucesso.")
    
    # Localização do SQL
    SCHEMA = "database/database.sql"

    # Declara o SQL para o banco
    with open(SCHEMA, 'r') as f:
        sql_script = f.read()

    # Executa cada statement do script SQL
    for statement in sql_script.split(';'):
        if statement.strip():  # Evita statements vazios
            try:
                cursor.execute(statement)
            except mysql.connector.Error as e:
                print(f"Erro ao executar statement: {e}")

    # Commit das operações
    conn.commit()
    print("Script executado com sucesso.")

except mysql.connector.Error as erro:
    print(f"Erro ao conectar ou executar operações no banco de dados: {erro}")

finally:
    # Garante que cursor e conexão serão fechados
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()
=======
from sqlalchemy import create_engine, Date, ForeignKey
from sqlalchemy.orm import Session, mapped_column, Mapped, DeclarativeBase, relationship, Session

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "tb_usuarios"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome:Mapped[str] = mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(nullable=False)
    senha:Mapped[str] = mapped_column(nullable=False)
    tasks = relationship("Task", backref= "user")

class Task(Base):
    __tablename__ = "tb_tasks"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome:Mapped[str] = mapped_column(nullable=False)
    descricao:Mapped[str] = mapped_column(nullable=False)
    status:Mapped[str] = mapped_column(nullable=False)
    data_de_criacao:Mapped[str] = mapped_column(Date, nullable=False)
    prazo:Mapped[str] = mapped_column(Date, nullable=False)
    prioridade:Mapped[str] = mapped_column(nullable=False)
    categoria:Mapped[str] = mapped_column(nullable=False)
    usu_id:Mapped[str] = mapped_column(ForeignKey("tb_usuarios.id"))

engine = create_engine('sqlite:///projeto.db')
session = Session(bind=engine)
Base.metadata.create_all(bind=engine)
>>>>>>> Stashed changes
