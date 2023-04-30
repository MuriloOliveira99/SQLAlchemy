CREATE DATABASE cinema
GO

USE cinema
GO

CREATE TABLE filmes (
	titulo VARCHAR(50) NOT NULL PRIMARY KEY,
	genero VARCHAR(30) NOT NULL,
	ano INT NOT NULL,
	
)
GO

INSERT INTO filmes(titulo, genero, ano)
VALUES ('Forrest Gump', 'Drama', 1994)
GO

SELECT * FROM filmes
GO