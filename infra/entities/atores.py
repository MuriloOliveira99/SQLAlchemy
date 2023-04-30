from infra.configs.base import Base 
from sqlalchemy import Column, String, Integer, ForeignKey


# classe representa a tabela do BD
class Atores(Base):
    __tablename__ = 'atores'

    # PK
    id = Column(Integer, primary_key = True)
    nome = Column(String(50), nullable = False)
    titulo_filme = Column(String, ForeignKey('filmes.titulo')) # FK

    # Retorna o OBJETO de uma forma LEGÍVEL
    def __repr__(self):
        return f'Atores [nome = {self.nome}, filme = {self.titulo_filme}]'