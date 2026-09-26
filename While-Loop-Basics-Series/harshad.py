#WAP to check whether a no. is harshad or not
n =int(input("Enter the no. ="))
s = 0
x =n
while n>0:
    rem=n%10
    s=s+rem
    n=n//10
if x%s==0:
    print("harshad no.")
else:
    print("not harshad no.")