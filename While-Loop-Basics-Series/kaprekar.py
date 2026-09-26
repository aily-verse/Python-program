#WAP to check the kaprekar no. using while loop
n = int(input("Enter the No. ="))
x=n
s=0
c=0
while n>0 :
    c=c+1
    n=n//10
p=pow(10,c)
sq=x*x
rem=sq%p
s=sq//p
if s+rem==x:
    print("kaprekar No.")
else :
    print("Not kaprekar No.")