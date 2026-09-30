while True:
    sayi = int(input("Bir sayı girin (çıkmak için 0 yazın): "))

    if sayi == 0:
        print("Program bitti.")
        break

    if sayi % 2 == 0:
        print(sayi, "çift bir sayıdır.")
    else:
        print(sayi, "tek bir sayıdır.")
