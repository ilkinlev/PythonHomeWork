userInput = int(input()) # 142
result = 0
userInput2 = userInput

while userInput > 0:
    digit = userInput % 10
    result  = result+digit
    userInput = int(userInput/10)

print(result)
input()