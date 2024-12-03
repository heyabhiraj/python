import matplotlib.pyplot as plt

def plot_cgpa_bar_chart():
    # Define the years and corresponding CGPA data
    years = ['10th', '12th', '1st Year', '2nd Year', '3rd Year']
    cgpa = [8.7, 9.1, 9.82, 9.36, 9.24]  # Example CGPA values for each year
    
    # Create the bar chart
    plt.bar(years, cgpa, color='skyblue')
    
    # Add title and labels
    plt.title("CGPA for Different Academic Years", fontsize=14)
    plt.xlabel("Academic Year", fontsize=12)
    plt.ylabel("CGPA", fontsize=12)
    
    # Optionally, display the CGPA values on top of each bar
    for i in range(len(cgpa)):
        plt.text(i, cgpa[i] + 0.05, str(cgpa[i]), ha='center', fontsize=10)
    
    # Show the plot
    plt.show()

# Call the function to display the bar chart
plot_cgpa_bar_chart()