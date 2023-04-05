import dbOlusturma as dbislem
from dbOlusturma import Kisi
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Query


# db bağlantı

engine = create_engine("sqlite:///rehber.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def ekle(ad, soyad, telefon):
    kisiEkle = dbislem.Kisi(ad=ad, soyad=soyad, numara=telefon)
    session.add(kisiEkle)
    session.commit()
    print("başarıyla eklendi")


def listele():
    kayitlar = session.query(Kisi).all()
    for kayit in kayitlar:
        """print(kayitlar.user_id, kayitlar.ad, kayitlar.soyad, kayitlar.numara)"""
        print(kayit)
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
