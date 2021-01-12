minInput = int(input("Min sayıyı yaz : "))
maxInput = int(input("Max sayıyı yaz : "))
stepInput = int(input("Step sayısını yaz : "))

array = []
sayi = minInput
maxSayi = maxInput + stepInput

while sayi <= maxInput:
    array.append(sayi)
    sayi = sayi + stepInput

print(array)
input()