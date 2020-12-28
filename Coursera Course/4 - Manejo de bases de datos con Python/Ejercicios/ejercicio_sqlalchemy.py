# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased

engine = create_engine('sqlite:///:memory:')

Base = declarative_base()


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, Sequence('author_id_seq'), primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    def __repr__(self):
        return "{} {}".format(self.firstname,self.lastname)

Author.__table__
Base.metadata.create_all(engine)

author = Author(firstname='firstname1',lastname='lastname1')
author2 = Author(firstname='firstname2',lastname='lastname2')
author3 = Author(firstname='firstname3',lastname='lastname3')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

session.add(author)
session.add(author2)
session.add(author3)

print(session.query(Author).filter(Author.firstname.like('firstname%')).count())

