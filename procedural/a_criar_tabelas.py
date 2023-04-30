'''
# SQLAlchemy
- O SQLAlchemy é um ORM completo, criado com Python para desenvolvedores de aplicativos, 
que fornece flexibilidade total do SQL, obtendo um conjunto completo de padrões de persistência
de nível corporativo bem conhecidos, que são projetados para acesso a banco de dados eficientes 
e de alto desempenho.
'''

# Importando a biblioteca SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Variaveis de conexao
SERVER = "DESKTOP-1EN88RT"
BANCO = "sqlalchemy"
DRIVER = "ODBC+Driver+17+for+SQL+Server"

# STRING de conexxao
CONN = f"mssql+pyodbc://{SERVER}/{BANCO}?trusted_connection=yes&driver={DRIVER}"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()

# Classe representa a tabela do banco de dados. 
class Pessoa(Base):
    __tablename__ = 'Pessoa' # nome da tabela
    
    id = Column(Integer, primary_key = True) # Coluna
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))

Base.metadata.create_all(engine)
