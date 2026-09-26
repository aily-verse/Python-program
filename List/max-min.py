#max(),min()
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the no. = ")))
print(li)
print("Maximum Element = ",max(li))
print("Minimum Element = ",min(li))