from sqlalchemy import Column, BigInteger, String, DateTime, Boolean,ForeignKey, Table, Text 
from src.db.base_class import Base
from sqlalchemy.orm import relationship
from datetime import datetime


post_tag = Table("post_tag",Base.metadata, 
                 Column('post_id', BigInteger, ForeignKey('post.id')),
                 Column('tag_id', BigInteger, ForeignKey('tag.id')))

class Post(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    published_at = Column(DateTime, nullable=True)
    published = Column(Boolean, default=False)
    author_id = Column(BigInteger, ForeignKey('author.id'))    
    
    #relacion
    #el back_populates, segundo parametro es un atributo de la tabla con la que va a tener relacion
    author = relationship("Author", back_populates='posts')
    
    #la relacion de M to M hay q hacer la tabla intermedia primero.
    #3 parametros, 1- relacion principal, 2- reacion secundaria(tabla de M to M, 3 backpopulates)
    tags = relationship('Tag', secondary=post_tag, back_populates='posts')
    