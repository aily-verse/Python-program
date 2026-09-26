#WAP to check whether a no. is disarium or not
n = int(input("Enter the no. = "))
x = n 
c = 0
s = 0
while n>0 :
    c = c +1
    n = n//10
n = x
while n>0 :
    rem = n%10
    s = s+pow(rem,c)
    n = n//10
    c = c -1
if s == x :
    print("disarium no.")
else :
    print("not disarium no.")