# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, Sequence('author_id_seq'), primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    def __repr__(self):
        return "{} {}".format(self.firstname,self.lastname)

engine = create_engine('sqlite:///:memory:')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

author = Author(firstname='Joanne',lastname='Rowling')

#session.add(author)

#our_author = session.query(Author).filter_by(firstname='Joanne').first()
#print(author is our_author)

#session.add_all([Author(firstname='John Ronald Reuel',lastname='Tolkien').Author(firstname='Jose',lastname='Hernandez')])

#session.new

#author.firstname='Joanne K.'

#session.dirty

#session.commit()

#author.id

#session.rollback()

#author.firstname

#another_author in session