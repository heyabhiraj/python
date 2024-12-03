import matplotlib.pyplot as plt

# Data: Water consumption categories and their percentages
labels = ['Drinking', 'Cooking', 'Bathing', 'Washing Clothes', 'Cleaning', 'Others']
sizes = [10, 15, 30, 25, 10, 10]  # Percentages of water consumption in daily life

# Colors for the pie chart
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Exploding the 2nd slice (Washing Clothes) to highlight it
explode = (0, 0.1, 0, 0, 0, 0)

# Plotting the pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, explode=explode)

# Adding a title to the pie chart
plt.title("Water Consumption in Daily Life")

# Displaying the pie chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
