#WAP to check the factorial no. using for loop
n = int(input("Enter the number = "))
fact = 1
if n < 0:
   print("Factorial does not exist")
elif n == 0:
   print("Factorial of 0 is 1")
else:
   for i in range(1,n+1,1):
       fact = fact*i
   print("The factorial of",n,"is",fact)
