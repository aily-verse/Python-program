'''
WAP to print the factor of a no.    
6---->1,2,3,6
'''
n = int(input(" Enter the No. = "))
print("Factor of",n,"is = ",end='')
for i in range(1,n+1,1) :
    if n%i ==0 :
        print(i,end=',')