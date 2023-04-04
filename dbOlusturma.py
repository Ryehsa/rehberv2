import sqlalchemy
from sqlalchemy import create_engine,Table,Integer,String,Column,Text,Identity
from sqlalchemy import MetaData
from sqlalchemy.exc import SQLAlchemyError

meta = MetaData()
engine = create_engine('sqlite:///rehber.db', echo = True)


rehber = Table(
   'kisiler', meta, 
   Column('userId', Integer,Identity(1,1)), 
   Column('ad', Text), 
   Column('soyAd', Text),
   Column('telefonNumarası', Text),
)
meta.create_all(engine)