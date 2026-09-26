'''
-------------------------------
ODD                EVEN 
-------------------------------
1                   2
3                   4
5                   6
'''
n = int(input("Enter the Range = "))
print("-------------------------------")
print("ODD\t\tEVEN")
print("-------------------------------")
for i in range (1,n+1,1) :
    if i%2 == 0 :
        print("\t",i)
    else :
        print(i,end = "\t")