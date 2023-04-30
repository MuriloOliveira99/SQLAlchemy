from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:

    def __init__(self) -> None:
        self.__server = 'DESKTOP-1EN88RT'
        self.__database = 'cinema'
        self.__driver = 'ODBC+Driver+17+for+SQL+Server'
        self.__connection_string = f"mssql+pyodbc://{self.__server}/{self.__database}?trusted_connection=yes&driver={self.__driver}"
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind = self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()