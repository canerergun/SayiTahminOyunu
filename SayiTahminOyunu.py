# Sayı Tahmin Oyunu
# Kullanıcının bilgisayar tarafından rastgele seçilen bir sayıyı tahmin etmesini gerektirir.
# Kullanıcının girdiği sayılar doğru sayıya yaklaştıkça, program kullanıcıya ipucu verir

import random
import time

sorguBool = True
computer = random.randint(1, 100)

while sorguBool:
    try:
        user = int(input("Sayı Giriniz: "))
        if user > computer:
            print("Sayı Büyük Tahminim Daha da Küçük")
        elif user < computer:
            print("Sayı Küçük Tahminim Daha da Büyük")
        elif user == computer:
            print("Doğru Tahmin!!!!")
            time.sleep(3)
            print("Oyun Başarılı bir şekilde sona erdi!")
            time.sleep(2)
            sorgu = input("Devam etmek için 'e' veya 'E' tuşlayın: ").lower()
            computer = random.randint(1, 100)
            if sorgu != "e":
                sorguBool = False
                print("Oyundan çıkılıyor!")
                time.sleep(3)
                print("Başarılı bir şekilde çıkış yapıldı!")




    except ValueError:
        print("Baba napıyon yaaaaa!!!!!!")
