#WAP to check whether a No. is Buzz or not
x = int(input("Enter the No. = "))
if x%7 == 0 or x%10 == 7 :
    print(x,"is Buzz No. ")
else : 
    print(x,"is not Buzz No. ")