import os 
os.system('cls')

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_ # Column, String, Integer    
from sqlalchemy.orm import sessionmaker
from infra.entities.filmes import Filmes


SERVER = "DESKTOP-1EN88RT"
BANCO = "cinema"
DRIVER = "ODBC+Driver+17+for+SQL+Server"

# STRING de conexxao
CONN = f"mssql+pyodbc://{SERVER}/{BANCO}?trusted_connection=yes&driver={DRIVER}"

# CONFIGURAÇÕES
engine = create_engine(CONN, echo = True)
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()


'''
############### CONSULTAS ###############
'''

# # Retorna todos os filmes
# filmes_all = session.query(Filmes).all()
# for filme in filmes_all:
#     print('-' * 50)
#     print(f'Filme: {filme.titulo}')
#     print(f'Genero: {filme.genero}')
#     print(f'Ano: {filme.ano}')    
# print('-' * 50)
# print('\n')

# # Retorna todos os filmes cujo genero == 'Drama'
# filmes_drama = session.query(Filmes).filter(Filmes.genero == 'Drama').all()
# for filme in filmes_drama:
#     print('-' * 50)
#     print(f'Filme: {filme.titulo}')
#     print(f'Genero: {filme.genero}')
#     print(f'Ano: {filme.ano}')
# print('-' * 50)
# print('\n')

# Retorna todos os filmes do genero == Drama e ano == 2000
# AND

# filmes_comedia_2000 = session.query(Filmes).filter(Filmes.genero == 'Comedia').filter(Filmes.ano == 2000).all()
# # filmes_comedia_2000 = session.query(Filmes).filter_by(genero = 'Comedia', ano = 2000)
# for filme in filmes_comedia_2000:
#     print('-' * 50)
#     print(f'Filme: {filme.titulo}')
#     print(f'Genero: {filme.genero}')
#     print(f'Ano: {filme.ano}')
# print('-' * 50)
# print('\n')

# Retorna todos os filmes do genero == Drama ou Ano == 2022
# OR
filmes_drama_ou_2022 = session.query(Filmes).filter(or_(Filmes.genero == 'Drama', Filmes.ano == 2022))
for filme in filmes_drama_ou_2022:
    print('-' * 50)
    print(f'Filme: {filme.titulo}')
    print(f'Genero: {filme.genero}')
    print(f'Ano: {filme.ano}')
print('-' * 50)
print('\n')

session.close()