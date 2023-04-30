from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filmes
from sqlalchemy.orm.exc import NoResultFound


class FilmesRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data
        
    # teste erro
    def select_drama_filmes(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Filmes).filter(Filmes.genero == 'huaduhda').one()
                return data
            except NoResultFound:
                return None 
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, titulo, genero, ano):
        with DBConnectionHandler() as db:
            try:
                data_insert = Filmes(titulo = titulo, genero = genero, ano = ano)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback() # volta o banco ao estado anterior
                raise exception # exibe o erro

    def delete(self, titulo):
        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db.session.commit()

    def update(self, titulo, ano):
        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).update({ "ano" : ano })
            db.session.commit()