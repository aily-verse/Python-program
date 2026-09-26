#WAP to check whwther a no. is neon or not
n =int(input("Enter the no. = "))
s = 0
sqr =pow(n,2)
print("square of digit = ",sqr)
while sqr >0:
    rem =sqr%10
    s=s+rem
    sqr=sqr//10
print("the sum of the digits =",s)
if s==n :
    print("neon no.")
else:
    print("not neon no.")