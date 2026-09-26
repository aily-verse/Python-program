#WAP to check whther a no. is prime or not(2nd)
n =int(input("Enter the no. = "))
c =0
for i in range(2,n,1):
    if n%i==0:
        c=1
        break
if c==1:
    print("not prime no.")
else:
    print("prime no.")