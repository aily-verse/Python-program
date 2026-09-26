#WAP to check whether a perfect no. or not using for loop
n = int(input("Enter the No. = "))
sum = 0
for i in range(1,n,1) :
    if n%i == 0 :
        sum = sum+i
if sum == n :
    print("Perfect No.")
else :
    print("Not Perfect No.")