import sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# db bağlantı
engine = create_engine("sqlite:///rehber.db", echo=True)
# model tanımlama
Base = declarative_base()
conn = engine.connect()


class Kisi(Base):
    __tablename__ = "kisiler"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String)
    ad = Column(String)
    soyad = Column(String)
    numara = Column(Integer)

    """ def __str__(self) -> str:
        return f"{self.ad} - {self.soyad} """

    """ def __repr__(self):
        return f"<Kisi(user_id={self.user_id}, ad='{self.ad}', soyad='{self.soyad}', numara={self.numara})>" """


# Veritabanını oluşturma
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
