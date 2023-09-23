from sqlmodel import SQLModel, Field, create_engine, Session, select, Relationship
from typing import Optional

# table = true -> utiliza o nome da classe para criar a tabela
class Person(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    name: str

    balance: "Balance" = Relationship(back_populates = "person")

class Balance(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    value: int 
    person_id: int = Field(foreign_key = "person.id")

    person: Person = Relationship(back_populates = "balance")

SERVER = "DESKTOP-1EN88RT"
BANCO = "sql_alchemy"
DRIVER = "ODBC+Driver+17+for+SQL+Server"
CONN = f"mssql+pyodbc://{SERVER}/{BANCO}?trusted_connection=yes&driver={DRIVER}"

engine = create_engine(CONN, echo = True)
SQLModel.metadata.create_all(bind = engine)

with Session(engine) as session:

    ##### INSERINDO DADOS ##### 
    person = Person(name = 'Oliveira')
    session.add(person)

    person = Person(name = 'Rocha')
    session.add(person)

    session.commit()

    #### CONSULTANDO OS DADOS ##### 
    sql = select(Person)
    results = session.exec(sql)

    for person in results:
        balance = Balance(value = 60, person = person)
        session.add(balance)
    session.commit()

    for person in results:
        print(person.name, person.balance[0].value)
    
    sql = select(Balance)
    results = session.exec(sql)
    for balance in results:
        print(balance.person)

    ### EX1. JOIN
    sql_join = select(Person, Balance).where(Balance.person_id == Person.id)
    results = session.exec(sql_join)
    for person, balance in results:
        print(person.name, balance.value)

    ### EX2. JOIN
    sql_join2 = select(Person, Balance).join(Balance, isouter = True)
    print(sql_join2)