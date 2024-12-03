import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def fit_poisson(data):
    # Calculate the mean (lambda) of the data
    lambd = np.mean(data)
    
    # Print the estimated lambda (mean) for the Poisson distribution
    print(f"Estimated lambda (mean) for Poisson distribution: {lambd}")
    
    # Generate the range of possible values for the Poisson distribution (0 to max(data))
    x_values = np.arange(0, int(np.max(data)) + 1)
    
    # Calculate the Poisson PMF for each value in x_values
    poisson_pmf = poisson.pmf(x_values, lambd)
    
    # Plot the histogram of the data
    plt.hist(data, bins=np.arange(0, int(np.max(data)) + 2) - 0.5, density=True, alpha=0.6, color='orange', label="Data Histogram")
    
    # Plot the fitted Poisson distribution
    plt.plot(x_values, poisson_pmf, 'ro-', label="Fitted Poisson Distribution")
    
    # Set the labels and title
    plt.xlabel("Data Value")
    plt.ylabel("Probability")
    plt.title("Poisson Distribution Fit")
    
    # Show the legend
    plt.legend()
    
    # Display the plot
    plt.show()

# Example dataset (counts of occurrences)
data = np.array([2, 3, 2, 1, 3, 4, 5, 2, 3, 1, 4, 3, 2, 4, 3, 3, 5, 2, 1])

# Fit the Poisson distribution on the given data
fit_poisson(data)
