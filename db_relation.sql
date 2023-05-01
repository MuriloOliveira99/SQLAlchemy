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


/*
INSERT INTO filmes(titulo, genero, ano)
VALUES
('A favorita', 'Drama', 2008),
('Nomadland', 'Drama', 2000),
('Daniel Blake', 'Drama', 1997),
('Tomates verdes', 'Drama', 2006),
('Volver', 'Drama', 1997),
('O pianista', 'Drama', 2014),
('Panico', 'Terror', 2002),
('Um lugar silencioso', 'Terror', 2002),
('Caçadores de Bruxas', 'Terror', 2008),
('Exorcista do Papa', 'Terror', 2022),
('Orfã 2', 'Terror', 2022),
('Peso do Talento', 'Terror', 2022),
('Shiva Baby', 'Comedia', 2014),
('Free Guy', 'Comedia', 2000),
('Bobs Burgers', 'Comedia', 2000),
('Jojo Rabbit', 'Comedia', 2023)
GO

INSERT INTO atores(nome, titulo_filme)
VALUES
('Maria', 'A favorita'),
('João', 'Nomadland'),
('Anna', 'Daniel Blake'),
('Murilo', 'Tomates verdes'),
('Anna', 'Volver'),
('Murilo', 'O pianista'),
('Maria', 'Panico'),
('João', 'Um lugar silencioso'),
('Anna', 'Caçadores de Bruxas'),
('Murilo', 'Exorcista do Papa'),
('Maria', 'Orfã 2'),
('João', 'Peso do Talento'),
('Murilo', 'Shiva Baby'),
('Anna', 'Free Guy'),
('João', 'Bobs Burgers'),
('Maria', 'Jojo Rabbit')

*/