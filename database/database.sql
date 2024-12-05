

CREATE TABLE IF NOT EXISTS tb_usuarios (
    usu_id INTEGER PRIMARY KEY  AUTOINCREMENT,
    usu_nome VARCHAR(200) NOT NULL,
    usu_email VARCHAR(200) NOT NULL,
    usu_senha VARCHAR(200) NOT NULL
);


CREATE TABLE IF NOT EXISTS tb_tarefas (
    tar_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tar_nome VARCHAR(1000) NOT NULL,
    tar_descricao VARCHAR(1000) NOT NULL,
    tar_status VARCHAR(1000) NOT NULL,
    tar_data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tar_prazo DATE NOT NULL,
    tar_prioridade VARCHAR(1000) NOT NULL,
    tar_categoria VARCHAR(1000) NOT NULL,
    tar_usuario_id INT NOT NULL,
    FOREIGN KEY (tar_usuario_id) references tb_usuarios(usu_id)
);