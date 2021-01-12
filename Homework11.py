num = int(input("Bir sayı yazın : "))

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num," sade bir sayı deyil")
           break
   else:
       print(num," sade bir sayıdır")
       
else:
   print(num," sade bir sayı deyil")
input()