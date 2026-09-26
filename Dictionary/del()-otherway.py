#del
x={}
n=int(input("Enter the Range = "))
for i in range(1,n+1,1):
    s=input("Enter the value as string = ")
    x[i]=s
print(x)
p=input("Enter the value you want to delete = ")
s=0
x={1:'sampoo',2:'mal',3:'aily',4:'palai'}
for k,v in x.items():
    if p==v:
        s=1
        break
if s==1:
    del(x[k])
    print(x)
else:
    print("deletion not possible") 