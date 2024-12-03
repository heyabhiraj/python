import csv
# Function to write data to a CSV file
def write_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Writing the headers (optional)
        writer.writerow(['Name', 'Age', 'Department'])
        # Writing the data
        writer.writerows(data)
    print(f"Data has been written to {filename} successfully.")

# Function to read data from a CSV file
def read_from_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        # Reading the header (optional)
        header = next(reader)
        print("Header:", header)
        
        # Reading and printing the rows
        print("\nData from the CSV file:")
        for row in reader:
            print(row)

# Data to be written to the CSV file
data_to_write = [
    ['John Doe', 29, 'Sales'],
    ['Jane Smith', 35, 'HR'],
    ['Tom Johnson', 42, 'IT'],
    ['Sara Lee', 28, 'Marketing']
]

# File name
csv_filename = 'employee_data.csv'

# Write data to the CSV file
write_to_csv(csv_filename, data_to_write)

# Read data from the CSV file
read_from_csv(csv_filename)