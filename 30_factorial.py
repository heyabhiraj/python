#WAP to find factorial using recursion. 

def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number to find its factorial: "))
result = factorial(num) # Calling the recursive function to print the result
print(f"The factorial of {num} is {result}")


def fact(n):
    if n==0 or n ==1:
        return 1
    else:
        return n * fact(n-1)
num = int(input("enter a no ."))
res=fact(num)
print( res)