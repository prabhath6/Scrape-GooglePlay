from sqlalchemy import create_engine, Column, BigInteger, String, Date, Float, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql
from sqlalchemy.engine.url import URL
import settings


Base = declarative_base()

def db_connect():
    """
    returns psql engine instance
    """
    return create_engine(URL(**settings.DATABASE))

def create_table(engine):
    """
    creates the tables
    """
    Base.metadata.create_all(engine)

class App_metrics(Base):

    __tablename__ = "messengers"

    id = Column(BigInteger, Sequence('seq_reg_id', start=1, increment=1), primary_key=True)
    title = Column('title', String)
    url = Column('url', String, nullable=True)
    rating = Column('rating', Float, nullable=True)
    rated_by = Column('rated_by', BigInteger, nullable=True)
    downloads = Column('downloads', BigInteger, nullable=True)
    download_range_min = Column('download_range_min', BigInteger, nullable=True)
    download_range_max = Column('download_range_max', BigInteger, nullable=True)
    last_updated = Column('last_updated', Date, nullable=True)
    rating_one = Column('rating_one', BigInteger, nullable=True)
    rating_two = Column('rating_two', BigInteger, nullable=True)
    rating_three = Column('rating_three', BigInteger, nullable=True)
    rating_four = Column('rating_four', BigInteger, nullable=True)
    rating_five = Column('rating_five', BigInteger, nullable=True)

