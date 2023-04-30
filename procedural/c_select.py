# Importando a biblioteca SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from a_criar_tabelas import Pessoa
from sqlalchemy import or_

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

pessoas = session.query(Pessoa).all() # retorna uma lista com todos os dados da tabela

# Retorna todos os dados da tabela
for pessoa in pessoas:
    print(f'ID: {pessoa.id}')
    print(f'Nome: {pessoa.nome}')
    print(f'Usuário: {pessoa.usuario}')
    print(f'Senha: {pessoa.senha}')
    print()
print(200 * '*')

#######################################
#  FILTRANDO DADOS - AND
#######################################
pessoas = session.query(Pessoa).filter(Pessoa.id == 4).filter(Pessoa.nome == 'João')
# pessoas = session.query(Pessoa).filter_by(id = 4, nome = 'João') # Outra forma de filtrar

for pessoa in pessoas:
    print(f'ID: {pessoa.id}')
    print(f'Nome: {pessoa.nome}')
    print(f'Usuário: {pessoa.usuario}')
    print(f'Senha: {pessoa.senha}')
    print()

print(200 * '*')
#######################################
#  FILTRANDO DADOS - OR
#######################################
pessoas = session.query(Pessoa).filter(or_(Pessoa.id == 1, Pessoa.senha == 'jaozin321')) # retorna o id 1 OU quem tem a senha == 'jaozin321'

for pessoa in pessoas:
    print(f'ID: {pessoa.id}')
    print(f'Nome: {pessoa.nome}')
    print(f'Usuário: {pessoa.usuario}')
    print(f'Senha: {pessoa.senha}')
    print()

