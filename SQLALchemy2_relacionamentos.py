from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase

class Base(DeclarativeBase):
    pass

# classe = representa a tabela
class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    name = Column(String(255), nullable = False)

class Balance(Base):
    __tablename__ = 'balance'

    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    value = Column(Integer, nullable = False)
    
    # relacionamento (fisico)
    person_id = Column(Integer, ForeignKey(Person.id))

    person = relationship('Person', foreign_keys = 'Balance.person_id')

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

# results = session.query(Person)
# for result in results:
#     balance = Balance(value = 40, person_id = result.id)
#     session.add(balance)

# session.commit()

# # JOIN
# results = session.query(Balance)
# for result in results:
#     print(result.value, result.person.name)

# # JOIN
results = session.query(Person.name, Balance.value).join(Balance, isouter = True)
for result in results:
    print(result)