import array

userInput = int(input("Sayıyı yazın : "))

fib = [ 1,1 ]

i = 2

while i <= userInput:
    fib.append(fib[i-1] + fib[i-2])
    i += 1

print(fib)
input()