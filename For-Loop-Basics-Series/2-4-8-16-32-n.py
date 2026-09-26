#WAP to print the series 2 4 8 16 32 ... n terms 
n = int(input("Enter the Range = "))
for i in range (1,n+1,1) :
    x = 2**i
    print(x,end =' ')