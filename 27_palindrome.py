value = str(input("Enter a string or number: "))

# Check if the value is a palindrome
if value == value[::-1]:
    print(f"{value} is a palindrome.")
else:
    print(f"{value} is not a palindrome.")
