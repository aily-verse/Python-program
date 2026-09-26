#WAP to implement slice operation
x=[]
x=input("Enter the string =")
print("String = ",x)
y=slice(3)    #0 to 2
print(x[y])
y=slice(3,6)    #3 to 5
print(x[y])
y=slice(3,len(x))    #3 to end
print(x[y])
y=slice(3,len(x),2)    #3 to end with step 2
print(x[y])