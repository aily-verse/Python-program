#clear(),pop(),del(),popitem()
x={1:'sampoo',2:'mal',3:'aily',4:'palai'}
for k,v in x.items():
    print(k,':',v)
x.clear()
print(x)
x={1:'sampoo',2:'mal',3:'aily',4:'palai'}
x.pop(2)
print(x)
del(x[3])
print(x)
x.popitem()
print(x)