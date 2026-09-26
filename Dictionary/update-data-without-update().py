#WAP to print the key value of a dictionary by using loop and update the data without update()
x={1:'sampoo',2:'mal',3:'aily',4:'palai'}
for k,v in x.item():
    print(k,':',v)
x[2]='rohit'
print(x)