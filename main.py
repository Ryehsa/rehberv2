import crudIslemleri as secimislem
import hashlib

giris_islem = int(input("İşlem Seçiniz : "))
print("1-Giris Yap")
print("2-Kayıt Ol")

if giris_islem == 1:
    print("giris islemi basarili")
elif giris_islem == 2:
    print("Kullanıcı adı : ")
    print("Sifre : ")

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
