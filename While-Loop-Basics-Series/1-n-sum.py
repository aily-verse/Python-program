#WAP to print 1-n & sum by using while loop
n = int(input("Enter the Range = "))
i = 1
s = 0
while i<=n :
    print(i,end=' ')
    s = s+i
    i = i+1
print("=",s)