CREATE DATABASE cinema 
GO

USE cinema 
GO 

CREATE TABLE filmes (
    titulo VARCHAR(50) NOT NULL,
    genero VARCHAR(30) NOT NULL,
    ano INT NOT NULL,
    PRIMARY KEY(titulo)
)
GO

CREATE TABLE atores (
    id INT IDENTITY(1, 1),
    nome VARCHAR(50) NOT NULL,
    titulo_filme VARCHAR(50) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (titulo_filme) REFERENCES filmes(titulo)
)
GO 

INSERT INTO filmes (titulo, genero, ano)
VALUES ('Forrest Gump', 'Drama', 1994)

INSERT INTO atores (nome, titulo_filme)
VALUES ('Tom Hanks', 'Forrest Gump')
GO