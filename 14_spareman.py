from scipy.stats import rankdata
def spearman_correlation(x, y):
    """
    Calculate the Spearman correlation coefficient between two lists of numbers.

    Args:
        x (list): First list of numbers.
        y (list): Second list of numbers.

    Returns:
        float: Spearman correlation coefficient.
    """
    if len(x) != len(y):
        raise ValueError("The two lists must have the same length.")

    n = len(x)
    if n == 0:
        raise ValueError("Lists must not be empty.")

    # Rank the data
    rank_x = rankdata(x)
    rank_y = rankdata(y)

    # Use Pearson correlation on the ranks
    mean_rank_x = sum(rank_x) / n
    mean_rank_y = sum(rank_y) / n

    numerator = sum((rank_x[i] - mean_rank_x) * (rank_y[i] - mean_rank_y) for i in range(n))
    denominator_x = sum((rank_x[i] - mean_rank_x) ** 2 for i in range(n)) ** 0.5
    denominator_y = sum((rank_y[i] - mean_rank_y) ** 2 for i in range(n)) ** 0.5

    if denominator_x == 0 or denominator_y == 0:
        raise ValueError("Standard deviation of one or both rank lists is zero.")

    return numerator / (denominator_x * denominator_y)

# Example usage
x = [10, 20, 30, 40, 50]
y = [12, 18, 33, 41, 49]

print(spearman_correlation(x, y))  # Output will depend on the ranking of x and y
