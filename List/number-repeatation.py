#WAP to count a no. how many times within a list
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(int(input("Enter the no. = ")))
print(li)
for i in li:
    print(i,end=',')
x=int(input("Enter the no. to be searched for = "))
print(x,"Found",li.count(x),"No. of times")