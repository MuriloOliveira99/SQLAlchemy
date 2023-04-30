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

pessoa = session.query(Pessoa).filter(Pessoa.id == 1).all()
pessoa[0].nome = 'Marcos'
pessoa[0].usuario = 'mrcos'
session.commit()