#WAP to find greatest of number using loop

n = int(input("Enter the number of elements: "))
greatest_number = None
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))       
    if greatest_number is None or num > greatest_number:
        greatest_number = num

print(f"The greatest number among {n} numbers is: {greatest_number}")

