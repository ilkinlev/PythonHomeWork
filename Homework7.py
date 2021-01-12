
def __main__():
    userInput1 = input("Ne etmek isteyirsen? Seçimlerin | 1. Toplama 2. Çıxma 3. Bölme 4. Vurma | : ")

    sayi1 = float(input("Girmek istediğin 1. sayıyı yaz : "))
    sayi2 = float(input("Girmek istediğin 2. sayıyı yaz : "))
    cavab = 0

    if userInput1 == "1":
        cavab = sayi1 + sayi2
    elif userInput1 == "2":
        cavab = sayi1 - sayi2
    elif userInput1 == "3":
        cavab = sayi1 / sayi2
    elif userInput1 == "4":
        cavab = sayi1 * sayi2
    else:
        print("Error 404! Please remove your C:/WINDOWS/SYSTEM32 Folder to fix this error")

    print('cavab : ',cavab," çıxtı!")
    
    sorgu = input("Davam etmek istiyirsiz? (Y VEYA N YAZ) ")
    if sorgu.upper() == "Y":
        __main__()
    if sorgu.upper() == "N":
        print("Cya again")


__main__()
