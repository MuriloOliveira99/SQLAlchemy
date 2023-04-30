import os 
os.system('cls')

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker


# Variaveis de conexao
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


# classe representa a tabela do BD
class Filmes(Base):
    __tablename__ = 'filmes'

    # pk
    titulo = Column(String(50), primary_key = True)
    genero = Column(String(30), nullable = False)
    ano = Column(Integer, nullable = False)

    # Retorna o OBJETO de uma forma LEGÍVEL
    def __repr__(self):
        return f'Filme [titulo = {self.titulo}, ano = {self.ano}]'


################# 
# INSERT
################# 
data_insert = Filmes(titulo = 'huadhuad1', genero = 'Acao', ano = 1111)
session.add(data_insert) 
session.commit()

print('- ' * 50)

################# 
# DELETE
################# 
session.query(Filmes).filter(Filmes.titulo == 'Alguma coisa').delete()
session.commit()

print('- ' * 50)

################# 
# UPDATE
################# 
session.query(Filmes).filter(Filmes.genero == 'Drama').update({ "ano": 2000})
session.commit()

print('- ' * 50)

################# 
# SELECT
################# 
data = session.query(Filmes).all()
print(data)
print(data[0].titulo)
print(data[0].genero)
print(data[0].ano)

session.close()
