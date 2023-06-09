import dbOlusturma as dbislem
from dbOlusturma import Kisi, KullaniciGiris
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib

# db bağlantı

engine = create_engine("sqlite:///rehber.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


# ilk girisi yapıcak kullanici ekleme
def kullanici_ekle(kullanici_adi, sifre):
    kayit_varmi = (
        session.query(Kisi)
        .filter(KullaniciGiris.kullanici_adi == kullanici_adi)
        .first()
    )
    if kayit_varmi:
        print("kullanıcı adı kayıtlı")
        quit()
    elif kayit_varmi == False:
        kullanici_kayit_ekle = dbislem.KullaniciGiris(
            kullanici_adi=kullanici_adi, password=sifre
        )
        session.add(kullanici_kayit_ekle)
        session.commit()
        print("başarıyla eklendi")


# kullanıcı giriş kontrol
def kullanici_giris(kullanici_adi, sifre):
    giris_kontrol = (
        session.query(Kisi)
        .filter(
            KullaniciGiris.kullanici_adi == kullanici_adi,
            KullaniciGiris.password == sifre,
        )
        .first()
    )
    if giris_kontrol:
        print("giriş başarılı")
    elif giris_kontrol == False:
        print("hatalı giriş")
        quit()


# rehbere ekleme
def ekle(ad, soyad, telefon, sifre):
    kisiEkle = dbislem.Kisi(ad=ad, soyad=soyad, numara=telefon, password=sifre)
    session.add(kisiEkle)
    session.commit()
    print("başarıyla eklendi")


# telefon numaralarını listeleme
def listele():
    kayitlar = session.query(Kisi).all()
    for kayit in kayitlar:
        print(
            kayit.user_id,
            kayit.ad,
            kayit.soyad,
            kayit.numara,
            kayit.password,
        )
    print("kayıtlar listelendi")


# rehber kayıt silme
def sil(user_id):
    sil = session.query(Kisi).filter(Kisi.user_id == user_id).delete()
    session.commit()
    print("başarıyla silindi")


# rehber kayıt güncelleme
def guncelle(ad, soyad, telefon, user_id):
    guncelle = (
        session.query(Kisi)
        .filter(Kisi.user_id == user_id)
        .update({Kisi.ad: ad, Kisi.soyad: soyad, Kisi.numara: telefon})
    )
    session.commit()
    print("kayıt güncellendi")


def sifreislemi(user_id, sifre):
    sifre = str(sifre)

    # kullanıcıdan alınan mevcut sifreyi encode etme
    """ sifreEslesme = hashlib.md5(sifre.encode("utf-8")).hexdigest() 
    print(sifreEslesme)"""
    ###########
    """ dbSifreBulma = session.query(Kisi).filter_by(user_id = user_id).first()
    mevcutEnCodeSıfre = dbSifreBulma.password """

    dbSifreBulma = session.query(Kisi).filter(Kisi.user_id == user_id).first()
    mevcutEnCodeSıfre = dbSifreBulma.password

    print(user_id, dbSifreBulma.ad)
    print(sifre)
    print(mevcutEnCodeSıfre)

    if sifre != mevcutEnCodeSıfre:
        print("Hatalı Şifre ")
    elif sifre == mevcutEnCodeSıfre:
        yeni_sifre = input("yeni sifre : ")
        yeni_sifre = hashlib.md5(yeni_sifre.encode("utf-8")).hexdigest()
        guncelle = (
            session.query(Kisi)
            .filter(Kisi.user_id == user_id)
            .update({Kisi.password: yeni_sifre})
        )
        session.commit()
