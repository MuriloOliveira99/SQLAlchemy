# Importando a biblioteca SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from a_criar_tabelas import Pessoa

def retorna_session():

    # Variaveis de conexao
    SERVER = "DESKTOP-1EN88RT"
    BANCO = "sqlalchemy"
    DRIVER = "ODBC+Driver+17+for+SQL+Server"

    # STRING de conexxao
    CONN = f"mssql+pyodbc://{SERVER}/{BANCO}?trusted_connection=yes&driver={DRIVER}"

    engine = create_engine(CONN, echo = True)
    Session = sessionmaker(bind = engine)
    
    return Session()

session = retorna_session() # instancia da funcao

pessoa = Pessoa(nome = 'Murilo', 
                usuario = 'mrl', 
                senha = '1234')

session.add(pessoa) # na session, adicione a pessoa
session.rollback() # limpar a session após adicao dos dados
session.commit() # com a pessoa adicionada na session, envie para o banco

# ENVIAR MAIS DE UM CADASTRO (PESSOA)
# pessoa = Pessoa(nome = 'Murilo', 
#                 usuario = 'mrl', 
#                 senha = '1234')

# pessoa2 = Pessoa(nome = 'Joao', 
#                 usuario = 'jao', 
#                 senha = '1432')

# session.add_all([pessoa, pessoa2]) 
# session.rollback() # limpar a session após adicao dos dados
# session.commit() 



