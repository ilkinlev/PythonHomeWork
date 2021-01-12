userChoice = input("1 = Rectangle | 2 = Triangle | 3 = Circle | Cevabınız : ")
sonuc = 0
pi = 3.14

if userChoice == "1":
    side1 = int(input("Qısa Side'ı yazin : "))
    side2 = int(input("Uzun Side'ı yazin : "))
    sonuc = side1*side2
elif userChoice == "2":
    base = int(input("yerin yüksekliğini girin : "))
    height = int(input("Yüksekliğini girin : "))
    sonuc = 0.5 * base * height
elif userChoice == "3":
    radius = int(input("Radius girin : "))
    sonuc = 2 * pi * radius
else:
    print("Program düzgün işlemedi! Bir daha sinayin!")
        
print('Sonuç : ', "%.2f" % sonuc)
input()