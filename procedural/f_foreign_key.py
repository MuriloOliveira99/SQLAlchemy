# Importando a biblioteca SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# variaveis de conexao
SERVER = "DESKTOP-1EN88RT"
BANCO = "sqlalchemy"
DRIVER = "ODBC+Driver+17+for+SQL+Server"

# string de conexao
CONN = f"mssql+pyodbc://{SERVER}/{BANCO}?trusted_connection=yes&driver={DRIVER}"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()

# CLASSE -> Representa a tabela do banco de dados
class Pessoa(Base):
    __tablename__ = 'pessoa' # nome da tabela

    # colunas da tabela
    id = Column(Integer, primary_key = True) 
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))

class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key = True)
    categoria = Column(String(50))

class Produto(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key = True)
    produto = Column(String(50))
    id_categoria = Column(Integer, ForeignKey('categoria.id'))

Base.metadata.create_all(engine)

# inserindo pessoa
pessoa = Pessoa(nome = 'Murilo',
                usuario = 'mrl',
                senha = '123')

# # inserindo categoria
categoria = Categoria(categoria = 'Fruta')

# inserindo produto
produto = Produto(produto = 'Maça',
                  id_categoria = 1)

session.add_all([pessoa, categoria, produto]) # adiciona os dados na session
session.commit() # envia para o banco