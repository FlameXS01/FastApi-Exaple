from sqlalchemy import Column, BigInteger, String, DateTime
from src.db.base_class import Base
from sqlalchemy.orm import relationship

class Author (Base):
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True) 
     
     
    #el backpopulate tiene q apuntar a donde esta la relacion en la otra tabla
    #tiene que estar en las dos tablas la relacion sea cual sea.
    posts = relationship("Post", back_populates='author')