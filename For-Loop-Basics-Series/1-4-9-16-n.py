#WAP to print the series 1 4 9 16 ... n terms 
n = int(input("Enter the Range = "))
s = 0
for i in range (1,n+1,1) :
    x = i*i
    print(x,end =' ')
    s = s + x 
print("=",s)