'''
WAP to print Fibonacci series
    0 1 1 2 3 5 8...n 
'''
n = int(input("Enter the Term = "))
a = 0 
b = 1
s = 0
print(a,b,end='')
for i in range(1,n-1,1) :
    s = a+b
    print(s,end='')
    a = b
    b = s 