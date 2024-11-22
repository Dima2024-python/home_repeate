from datetime import datetime

from sqlalchemy import Column, Text, Integer, Float, DateTime, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import config


Base = declarative_base()


class Product(Base):
    __tablename__ = 'Products'

    id = Column(Integer, primary_key=True)
    image = Column(String, default="")
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False, default='')
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    your_data = Column(Text, nullable=False, default='Данні продавця не вказано')


engine = create_engine(config.DB_PATH, echo=config.DEBUG)

Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    Base.metadata.create_all(engine)
