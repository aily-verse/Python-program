#WAP to print 1- n even range & sum
n = int(input("Enter the Range = "))
s = 0
for i in range (2,n+1,2) :
    print(i,end =' ')
    s = s + i
print("=",s)