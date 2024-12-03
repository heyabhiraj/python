#WAP to print fibonacci series. 

n = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1 #starting values of fibonacci series
print(f"Fibonacci Series of {n} terms:")
for i in range(n):
    print(a, end=" ") 
    a, b = b, a + b
