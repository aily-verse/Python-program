#WAP to store n element of integer type within list and sort the list 
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the no. = ")))
print(li)
li.sort()
print("List = ",li)