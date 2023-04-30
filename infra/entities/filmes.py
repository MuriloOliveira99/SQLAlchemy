from infra.configs.base import Base 
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


# classe representa a tabela do BD
class Filmes(Base):
    __tablename__ = 'filmes'

    # pk
    titulo = Column(String(50), primary_key = True)
    genero = Column(String(30), nullable = False)
    ano = Column(Integer, nullable = False)

    # Relacao reversa
    # mostra todos os atores do filme 
    # *nao eh tao performatico
    atores = relationship('Atores', backref = 'atores', lazy = 'subquery')

    # Retorna o OBJETO de uma forma LEGÍVEL
    def __repr__(self):
        return f'Filme [titulo = {self.titulo}, ano = {self.ano}]'