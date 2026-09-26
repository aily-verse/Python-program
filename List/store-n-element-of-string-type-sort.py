#WAP to store n element of string type within list and sort the list 
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(input("Enter your name = "))
print(li)
li.sort()
print(li)