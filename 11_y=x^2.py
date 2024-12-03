#WAP to plot a graph for function (y=x^2).

#Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.linspace(-10, 10, 400)  # 400 points between -10 and 10

# Define the function y = x^2
y = x**2

# Create the plot
plt.plot(x, y,color='purple')

# Add title and labels
plt.title("Graph for function y = x\N{superscript two}")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

# Show the plot
plt.grid(True)
plt.show()
