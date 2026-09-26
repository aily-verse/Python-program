#WAP to check whether a no. is autopolymorphic or not
x = int(input("Enter the No. = "))
if ((x*x)%10)==x or ((x*x)%100)==x :
    print("Autopolymorphic No.")
else :
    print("Not Autopolymorphic No.")