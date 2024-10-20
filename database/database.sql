CREATE DATABASE IF NOT EXISTS db_gerenciamento;
USE db_gerenciamento;

CREATE TABLE IF NOT EXISTS tb_usuarios (
    usu_id INT(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    usu_nome VARCHAR(200) NOT NULL,
    usu_email VARCHAR(200) NOT NULL,
    usu_senha VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_tarefas (
    tar_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    tar_nome TEXT NOT NULL,
    tar_descricao TEXT NOT NULL,
    tar_status TEXT NOT NULL,
    tar_data_criacao DATE DEFAULT (CURDATE()) NOT NULL,
    tar_prazo DATE NOT NULL,
    tar_prioridade TEXT NOT NULL,
    tar_categoria TEXT NOT NULL,
    tar_usuario_id INT NOT NULL,
    FOREIGN KEY (tar_usuario_id) references tb_usuarios(usu_id)
);