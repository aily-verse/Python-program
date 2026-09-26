#WAP to print the series 1 11 111 1111... n terms & sum
n = int(input("Enter the Range = "))
j = 1
s = 0
for i in range (1,n+1,1) :
    print(j,end =' ')
    s = s + j 
    j = j*10+1
print("=",s)