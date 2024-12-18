import mysql.connector as sql

def obter_conexao():
<<<<<<< Updated upstream
    db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'db_gerenciamento'
    }
    conn = sql.connect(**db_config, auth_plugin='mysql_native_password')
    
    return conn
=======
    conn = sqlite3.connect("projeto.db")
    conn.row_factory = sqlite3.Row
    return conn 
>>>>>>> Stashed changes
