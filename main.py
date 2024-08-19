def tas_kagit_makas_Hacer_Ozcan():
    print("Selamlaaaarr \nTaş, Kağıt, Makas oyununa hoş geldiniz.")
    print("Oyun kuralları:\n 1. Taş, makası yener\n 2. Makas, kağıdı yener\n 3. Kağıt, taşı yener")
    print("Galibiyet için iki turu kazanman lazım..   Unutma bu şans oyunu değil, iyi olan kazansın ;) ")
    print("Başlamak için seçim yapmalısın taş için 't', kağıt için 'k', makas için 'm' seçin ")
    print("Oyundan çıkmak için 'q' yazabilirsiniz.")

    secim = ['t', 'k', 'm']
    secim_2 = ['e', 'h']

    while True:
        senin_skorun = 0
        bilgisayar_skoru = 0

        while senin_skorun < 2 and bilgisayar_skoru < 2:
            senin_secim = input("Seçiminizi yapın (taş/kağıt/makas): ").lower()
            pc_secim = random.choice(secim)
            if senin_secim == 'q' or pc_secim == 'q':
                print("Oyun bitti, yeniden bekleriz :)")
                return
            if senin_secim not in secim:
                print("Geçersiz seçim Lütfen 't', 'k' veya 'm' girin.")
                continue

            pc_secim = random.choice(secim)
            print(f"Bilgisayarın seçimi: {pc_secim}")

            if senin_secim == pc_secim:
                print("Berabere ")
            elif (senin_secim == 't' and pc_secim == 'm') or \
                    (senin_secim == 'm' and pc_secim == 'k') or \
                    (senin_secim == 'k' and pc_secim == 't'):
                print("Kazandınnnn :D ")
                senin_skorun += 1
            else:
                print("Bilgisayar kazandı :)")
                bilgisayar_skoru += 1

            print(f"Skor - Siz: {senin_skorun}, Bilgisayar: {bilgisayar_skoru}")

        if senin_skorun == 2:
            print("Galibiyet Senin tebriler")
        else:
            print("Galibiyet Bilgisayarın Tebrikler")

        senin_secim2 = input("Bir el daha ??? (evet içim e /hayır için h basın) ").lower()
        pc_secim2 = random.choice(secim_2)
        if senin_secim2 == 'h' or pc_secim2 == 'h':
            print("Oyunu bitirdiniz. Güle güle!")
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import random
    tas_kagit_makas_Hacer_Ozcan()
