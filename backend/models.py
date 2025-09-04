from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    event_type = Column(String)

engine = create_engine('sqlite:///eventease.db')
Base.metadata.create_all(engine)
