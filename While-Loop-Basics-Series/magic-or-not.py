#WAP to check whether a no. is magic or not
n =int(input("Enter the no. = "))
s = 0
p =0
while n>0:
    rem=n%10
    s = s+rem
    n =n//10
x = s
while x>0:
    remainder =x%10
    p = p+remainder
    n =n//10
if s==p:
    print("magic no.")
else:
    print("not magic no.")