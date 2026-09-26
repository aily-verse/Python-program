#WAP to check whether a no. is armstrong or not
n = int(input("Enter the no. = "))
x = n 
c = 0
s = 0
while n>0 :
    c = c+1
    n = n//10
n = x
while n>0 :
    rem = n%10
    s = s+pow(rem,c)
    n = n//10
if s == x :
    print("armstrong no.")
else :
    print("not armstrong no.")