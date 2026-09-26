#Implement tuple 
t1=()
n=int(input("Enter the range = "))
for i in range (0,n,1):
    x=int(input("Enter the no. = "))
    t1=t1+(x,)
print(t1)
#t1[3]=40
#print(t1)