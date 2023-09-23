from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

class Base(DeclarativeBase):
    pass

# classe = representa a tabela
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    name = Column(String(255), nullable = False)

SERVER = "DESKTOP-1EN88RT"
BANCO = "sql_alchemy"
DRIVER = "ODBC+Driver+17+for+SQL+Server"
CONN = f"mssql+pyodbc://{SERVER}/{BANCO}?trusted_connection=yes&driver={DRIVER}"

# criando a conexao com banco de dados
engine = create_engine(CONN)

# Faz a criação da tabela (Person)
Base.metadata.create_all(bind = engine)

# manipulando o banco
Session = sessionmaker(autocommit = False, 
                       autoflush = False,
                       bind = engine)

session = Session()

####### INSERINDO DADOS #######
# person = Person(name = 'João')
# session.add(person)

# person = Person(name = 'Joana')
# session.add(person)

# session.commit()
# session.close()

####### CONSULTANDO OS DADOS #######
# results = session.query(Person).filter(Person.name == "Murilo")
results = session.query(Person).filter()
for result in results:
    print(result.id, result.name)

