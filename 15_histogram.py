import matplotlib.pyplot as plt
def plot_histogram(data, bins=10, title="Histogram", xlabel="Values", ylabel="Frequency"):
    """
    Plot a histogram for a list of numbers.

    Args:
        data (list): List of numbers to plot.
        bins (int): Number of bins in the histogram.
        title (str): Title of the plot.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
    """
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=bins, color='maroon', edgecolor='black', alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Example usage
data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 9]
plot_histogram(data, bins=8, title="Number Distribution", xlabel="Number Range", ylabel="Count")
