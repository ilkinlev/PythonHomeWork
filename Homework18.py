userInput = int(input("Sayi yazin : "))

cavab = 0

for i in range(1, userInput+1):
    cavab = i + cavab

print(cavab)
input()
