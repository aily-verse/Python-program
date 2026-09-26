#WAP to reverse the list(string),insert,pop
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(input("Enter the string = "))
print(li)
li.reverse()
print(li)
li.insert(3,'rana')
print(li)
li.pop()
print(li)