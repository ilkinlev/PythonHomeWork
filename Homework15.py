yazi = input("YAZI YAZ : ")

yazi = yazi.casefold()

rev_str = reversed(yazi)

if list(yazi) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
input()