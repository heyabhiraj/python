#WAP to demonstrate zero division error exception handling in python

a=int(input("Enter Numerator: "))
#exception handling
try:
    b=int(input("Enter Denominator: "))
    c=a/b
    print(f"Answer is {c}")
except:
    print("You have entered wrong input for Denominator \nSo the Program is Terminating")
