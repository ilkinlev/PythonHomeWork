from math import sqrt

sayi1 = int(input("İlk Sayıyı Yazın "))
sayi2 = int(input("İkinci Sayıyı Yazın "))
sayi3 = sqrt(sqrt(sayi1) + sqrt(sayi2))

perim = sayi1 + sayi2 + sayi3
findSides = (sayi1 + sayi2 + sayi3)/2
area = (findSides*(findSides-sayi1)*(findSides-sayi2)*(findSides-sayi3)) ** 0.5

print('Perimetr',format(perim,'.1f'))
print('Area',format(area,'.1f'))
input()
