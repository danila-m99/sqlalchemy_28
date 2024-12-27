from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime, timezone
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

# Базовый класс для всех моделей
Base = declarative_base()

# Модель Author
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)  # Идентификатор автора
    name = Column(String, nullable=False)  # Имя автора
    books = relationship("Book", back_populates="author")  # Связь с книгами

# Модель Book
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)  # Идентификатор книги
    title = Column(String, nullable=False)  # Название книги
    author_id = Column(Integer, ForeignKey('authors.id'))  # Внешний ключ на автора
    author = relationship("Author", back_populates="books")  # Связь с автором
    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # Ограничение уникальности
    


#class Order(Base):
#    __tablename__ = 'orders'
#    id = Column(Integer, primary_key=True)
#    product_name = Column(String, nullable=False)
#    quantity = Column(Integer, nullable=False)
#    created_at = Column(sa.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=True)  # Новое поле