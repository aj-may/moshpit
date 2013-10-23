from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()

class Pit(Base):
	__tablename__ = 'pits'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	host = Column(String)
	port = Column(Integer)

	def __repr__(self):
		return "%s    %s:%i" % (self.name, self.host, self.port)

Pit.metadata.create_all(create_engine('sqlite:///moshpit.db'))