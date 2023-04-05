import dbOlusturma as dbislem
from dbOlusturma import Kisi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Query
import hashlib

# db bağlantı

engine = create_engine("sqlite:///rehber.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def ekle(ad, soyad, telefon,sifre):
    
    kisiEkle = dbislem.Kisi(ad=ad, soyad=soyad, numara=telefon,password=sifre)
    session.add(kisiEkle)
    session.commit()
    print("başarıyla eklendi")


def listele():
    kayitlar = session.query(Kisi).all()
    for kayit in kayitlar:
        print(kayitlar.user_id, kayitlar.ad, kayitlar.soyad, kayitlar.numara,kayitlar.password) 
        
    print("kayıtlar listelendi")


def sil(user_id):
    sil = session.query(Kisi).filter(Kisi.user_id == user_id).delete()
    session.commit()
    print("başarıyla silindi")


def guncelle(ad, soyad, telefon, user_id):
    guncelle = (
        session.query(Kisi)
        .filter(Kisi.user_id == user_id)
        .update({Kisi.ad: ad, Kisi.soyad: soyad, Kisi.numara: telefon})
    )
    session.commit()
    print("kayıt güncellendi")
