#WAP to check whether a string is palindrome or not
x =input("Enter the string = ")
y = x[:: - 1]
print(y)
if x.lower() ==  y.lower() :
    print("Palindrome string")
else :
    print("Not palindrome string")