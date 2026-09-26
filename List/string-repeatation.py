#WAP store n element of string type within list and search how many times 
li=[]
n=int(input("Enter the Range = "))
for i in range(0,n,1):
    li.append(input("Enter your name = ").lower())
print(li)
x=input("\nEnter the string to be searched for = ").lower()
print(li.count(x),"No. of times")