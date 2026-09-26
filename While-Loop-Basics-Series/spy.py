#WAP to check whether a no. is spy or not using while loop
n =int(input("Enter the no. = "))
s = 0
p =1
while n>0:
    rem=n%10
    s = s+rem
    p = p*rem
    n =n//10
if s==p:
    print("spy no.")
else:
    print("not spy no.")