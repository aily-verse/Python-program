#WAP to print n-1 & sum by using while loop
n = int(input("Enter the Range = "))
i = n
s = 0
while i>=1 :
    print(i,end=' ')
    s = s+i
    i = i-1
print("=",s)