#WAP to find if a number is armstrong or not.

num = int(input("Enter a number to check if it is an Armstrong: "))
# Converting the number to a string to get the number of digits
num_str = str(num)
num_digits = len(num_str)
    
# Calculate the sum of the digits raised to the power of num_digits
sum_of_powers = sum(int(i) ** num_digits for i in num_str)

# sop= sum(int(j) ** num_digits for i in num_str)
    
# Check if the sum of powers equals the original number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
