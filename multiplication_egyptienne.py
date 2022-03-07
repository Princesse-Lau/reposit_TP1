from re import A


a = int (input ("a = "))
b = int (input ("b = "))

result = 0

while (b>0):
    if (b%2 == 0):
        a += a
        b /= 2
    else:
        result += a
        b -= 1

print(result)