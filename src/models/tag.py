from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from src.db.base_class import Base
from sqlalchemy.orm import relationship
from src.models.post import post_tag

class Tag(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    posts = relationship("Post", secondary= post_tag ,back_populates="tags")
    