a = int( input ("a = "))
n = int( input ("n = "))

print("\nu0 =",a)

for i in range(1, n+1):
    if a%2 == 0:
        a = a//2
    else:
        a = 3*a+1
    print("u%d = %d" %(i,a))