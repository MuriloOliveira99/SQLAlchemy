from infra.configs.connection import DBConnectionHandler
from infra.entities.atores import Atores
from infra.entities.filmes import Filmes

class AtoresRepository:
    def select(self):
        with DBConnectionHandler() as db:
            # data = db.session.query(Atores).all()
            data = db.session\
                    .query(Atores, Filmes)\
                    .join(Filmes, Atores.titulo_filme == Filmes.titulo)\
                    .with_entities(
                        Atores.nome, # exibe a coluna nome
                        Filmes.genero, # exibe a coluna genero
                        Filmes.titulo # exibe a coluna titulo
                    )\
                    .all()
            return data
