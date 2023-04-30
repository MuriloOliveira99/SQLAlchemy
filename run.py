'''
Os arquivos __init__.py são necessários para que o 
Python trate diretórios contendo o arquivo como pacotes
'''

from infra.repository.filmes_repository import FilmesRepository
from infra.repository.atores_repository import AtoresRepository


# Instancia da clase FilmesRepository
# que possuem os metodos CRUD
repo = FilmesRepository()

# SQL

# FILMES 
repo.insert('PPPO', 'comedia', 2010)
repo.delete('huadhuad1')
repo.update('huadhuad', 2000)
data = repo.select()
print(data)


# ATORES
repo2 = AtoresRepository()
response2 = repo2.select()
print(response2)

print('-' * 50)

# FILMES 
repo3 = FilmesRepository()
response3 = repo3.select()
print(response3)

print('-' * 50)

filme = response3[0]
print(filme.titulo)
print(filme.atores)

# SIMULANDO ERRO
simula_erro = FilmesRepository()
erro = simula_erro.select_drama_filmes()
print(erro)
