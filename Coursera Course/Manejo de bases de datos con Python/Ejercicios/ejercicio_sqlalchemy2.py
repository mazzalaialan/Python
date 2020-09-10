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

    books = relationship("Book", order_by="Book.id", back_populates="author")

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

autor1 = Author(firstname='firstname1', lastname='lastname1')
autor2 = Author(firstname='firstname2', lastname='lastname2')
autor3 = Author(firstname='firstname3', lastname='lastname3')
#print(autor1.books)
#print(autor2.books)
#print(autor3.books)

autor2.books = [Book(isbn='isbn1', title='title1', description='blablalbabllbvlllabvlba'),
                Book(isbn='isbn3', title='title3', description='blablalbasfaafssaflabvlba')]
                
autor3.books = [Book(isbn='isbn2', title='title2', description='blablalbabllbvlllabvlba')]

#print(autor2.books[1])
#print(autor2.books[1].title)

session.add(autor1)
session.add(autor2)
session.add(autor3)
session.commit()

print(session.query(Author.firstname).filter(Author.books.any()).count())

