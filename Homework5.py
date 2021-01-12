try:
	n = int(input('Sayi yaz : '))
	cevireleceksayi = int(str(n)[::-1])
	print(cevireleceksayi)
except ValueError:
	print('Yazdiginiz bir sayi deyil!')
input()
