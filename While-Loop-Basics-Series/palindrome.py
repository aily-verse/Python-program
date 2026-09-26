#WAP to check whether a no. is palindrome or not using while loop
n = int(input("Enter the No. ="))
rev = 0
x = n
while n>0 :
    rem = n%10
    rev = rev*10+rem
    n = n//10
if x == rev :
    print("Palindrome No.")
else :
    print("Not Palindrome No.")