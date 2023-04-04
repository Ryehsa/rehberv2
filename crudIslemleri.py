import sqlalchemy
from sqlalchemy import create_engine,Table,Integer,String,Column,Text,Identity
from sqlalchemy import MetaData


engine = create_engine('sqlite:///rehber.db', echo = True)
meta = MetaData()
conn=engine.connect()

rehber = Table(
   'kisiler', meta, 
   Column('userId', Integer,Identity(1,1)), 
   Column('ad', Text), 
   Column('soyAd', Text),
   Column('telefonNumarası', Text),
)
#meta.create_all(engine)

def ekle(ad,soyad,telefon):
    ins = rehber.insert().values(ad,soyad,telefon)
    result = conn.execute(ins)

    
    print("başarıyla eklendi")

def sil(user_id):
    print("başarıyla silindi")

def listele():
    print("kayıtlar listelendi")

def guncelle(ad,soyad,telefon,user_id):
    print("kayıt güncellendi")