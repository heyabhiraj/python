import math

# Function to compute sin(x) using Taylor series expansion
def sin_taylor(x, terms=10):
    result = 0
    for n in range(terms):
        term = ((-1)**n) * (x**(2*n+1)) / math.factorial(2*n+1)
        result += term
    return result

# Input value for x (in radians)
x = float(input("Enter the value of x in radians: "))

# Compute sin(x) using the Taylor series
sin_x = sin_taylor(x)

# Display the result
print(f"sin({x}) computed using Taylor series: {sin_x}")

