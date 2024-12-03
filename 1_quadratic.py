#WAP to find roots of a Quadratic Equation

import math
#taking input from user
a=int(input("Enter Coefficient of x\N{superscript two}: "))
b=int(input("Enter Coefficient of x: "))
c=int(input("Enter Constant term: "))
D=(b*b)-(4*a*c) #to compute the discriminant
if D>0:
    root1=(-b+math.sqrt(D))/(2*a)
    root2=(-b-math.sqrt(D))/(2*a)
    print("Roots are Real and Distinct:" ,root1,"and",root2)
elif D==0:
    root=(-b)/(2*a)
    print(f"Roots are Real and Equal, Root={root}")
else:
    re=(-b)/(2*a)
    img=math.sqrt(-D)/(2*a)
    print(f"Roots are imaginary, Root={re}+{img}i")
