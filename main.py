import crudIslemleri as secimislem
import hashlib

print("1-Giris Yap")
print("2-Kayıt Ol")
giris_islem = int(input("İşlem Seçiniz : "))

# giris yapma islemi
if giris_islem == 1:
    kullanici_adi = input("kullanıcı adı : ")
    sifre = input("Şifre : ")
    sifre_hash = hashlib.md5(sifre.encode("utf-8")).hexdigest()
    secimislem.kullanici_giris(kullanici_adi, sifre_hash)
# kayıt olma işlemi
elif giris_islem == 2:
    kullanici_adi = input("Kullanıcı adı : ")
    sifre = input("Sifre : ")
    sifre_hash = hashlib.md5(sifre.encode("utf-8")).hexdigest()
    secimislem.kullanici_ekle(kullanici_adi, sifre_hash)
else:
    print("Hatalı Seçim")
    quit()

print(
    " 1- Kayıt Ekle \n 2- Kayıt Sil\n 3- Kayıt Güncelle \n 4- Kayıt Listele\n5- Sifre guncelleme"
)
islem = int(input("İşlem Seçiniz : "))


# kayıt ekleme
if islem == 1:
    ad = input("Ad : ")
    soyad = input("Soyad : ")
    numara = int(input("Numara : "))
    sifre = input("Sifre : ")
    sifre_hash = hashlib.md5(sifre.encode("utf-8")).hexdigest()
    secimislem.ekle(ad, soyad, numara, sifre_hash)

# kayıt sil
elif islem == 2:
    secimislem.listele()
    id = int(input("Id seçiniz : "))
    print("Silinecek Kayıt Seçiniz : ")
    secimislem.sil(id)

# kayıt güncelle
elif islem == 3:
    secimislem.listele()
    id = int(input("Id seçiniz : "))
    ad = input("Ad : ")
    soyad = input("Soyad : ")
    numara = int(input("Numara : "))
    secimislem.guncelle(id, ad, soyad, numara)
# kayıt listele
elif islem == 4:
    secimislem.listele()
# sifre guncelleme
elif islem == 5:
    secimislem.listele()
    id = int(input("Id seçiniz : "))
    sifre = input("Mevcut Sifre : ")
    sifre = hashlib.md5(sifre.encode("utf-8")).hexdigest()
    print(sifre)
    secimislem.sifreislemi(id, sifre)
else:
    print("hatalı seçim")
