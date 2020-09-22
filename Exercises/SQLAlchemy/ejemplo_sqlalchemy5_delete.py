# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine('sqlite:///:memory:')

Base = declarative_base()

class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, Sequence('author_id_seq'), primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    books = relationship("Book", order_by="Book.id", back_populates="author", cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "{} {}".format(self.firstname,self.lastname)

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    isbn = Column(String)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey('author.id'))

    author = relationship("Author",back_populates="books")

    def __repr__(self):
        return "{}".format(self.title)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

j_rowling = Author(firstname='Joanne', lastname='Rowling')
print(j_rowling.books)

j_rowling.books = [Book(isbn='979884085674', title='Harry Potter y la Piedra Filosofal', description='blablalbabllbvlllabvlba'),
                   Book(isbn='979884085651', title='Harry Potter y la Camara Secreta', description='blablalbasfaafssaflabvlba')]

session.add(j_rowling)
session.commit()

print('pre Cant Autor',session.query(Author).filter_by(firstname='Joanne').count())
print('pre Cant Libros',session.query(Book).filter(Book.isbn.in_(['979884085674','979884085651'])).count())

session.delete(j_rowling)

print('post Cant Autor',session.query(Author).filter_by(firstname='Joanne').count())
print('post Cant Libros',session.query(Book).filter(Book.isbn.in_(['979884085674','979884085651'])).count())