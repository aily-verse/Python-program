#WAP to print the multiplication table of the no.
n =int(input("Enter the no. ="))
print("--------------------------------")
print("\t Multiplication Table")
print("--------------------------------")
for i in range(1,11,1):
    m = i*n
    print("\t",n,"*",i,"=",m)