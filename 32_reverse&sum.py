# Write a menu driven program to find the reverse of a number and sum of digits.

# Function to reverse a number
def reverse_number(num):
    return int(str(num)[::-1])

# Function to find the sum of digits of a number
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

print("\nMenu:")
print("Enter 1 to find the reverse of a number")
print("Enter 2 to find the sum of digits of a number")
print("Enter 3 to exit")
        
# Take user input for the menu choice
choice = int(input("Enter your choice (1/2/3): "))
        
if choice == 1:
    num = int(input("Enter a number to reverse: "))
    print(f"The reverse of {num} is {reverse_number(num)}")
        
elif choice == 2:
    num = int(input("Enter a number to find the sum of digits: "))
    print(f"The sum of digits of {num} is {sum_of_digits(num)}")
        
elif choice == 3:
    print("Exiting the program.")
    
else:
    print("Invalid choice. Please try again.")

