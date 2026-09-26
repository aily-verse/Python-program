#WAP to print n - 1 range & sum
n = int(input("Enter the Range = "))
s = 0
for i in range (n,0,-1) :
    print(i,end =' ')
    s = s +i
print("=",s)