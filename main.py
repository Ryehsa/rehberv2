import crudIslemleri as secimislem
import hashlib


print(" 1- Kayıt Ekle \n 2- Kayıt Sil\n 3- Kayıt Güncelle \n 4- Kayıt Listele")
islem = int(input("İşlem Seçiniz : "))


# kayıt ekleme
if islem == 1:
    ad = input("Ad : ")
    soyad = input("Soyad : ")
    numara = int(input("Numara : "))
    sifre = input("Sifre : ")
    sifre=hashlib.md5(sifre.encode()).hexdigest()
    secimislem.ekle(ad, soyad, numara,sifre)

# kayıt sil
elif islem == 2:
    secimislem.listele()
    id = int(input("Id seçiniz : "))
    print("Silinecek Kayıt Seçiniz : ")
    secimislem.Sil(id)

# kayıt güncelle
elif islem == 3:
    secimislem.listele()
    id = int(input("Id seçiniz : "))
    ad = input("Ad : ")
    soyad = input("Soyad : ")
    numara = int(input("Numara : "))
    sifre = input("Sifre : ")
    secimislem.guncelle(id, ad, soyad, numara,sifre)
# kayıt listele
elif islem == 4:
    secimislem.listele()
else:
    print("hatalı seçim")
