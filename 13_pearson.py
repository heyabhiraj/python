def pearson_correlation(x, y):
    """
    Calculate the Pearson correlation coefficient between two lists of numbers.

    Args:
        x (list): First list of numbers.
        y (list): Second list of numbers.

    Returns:
        float: Pearson correlation coefficient."""
    if len(x) != len(y):
        raise ValueError("The two lists must have the same length.")

    n = len(x)
    if n == 0:
        raise ValueError("Lists must not be empty.")

    mean_x = sum(x) / n
    mean_y = sum(y) / n

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator_x = sum((x[i] - mean_x) ** 2 for i in range(n)) ** 0.5
    denominator_y = sum((y[i] - mean_y) ** 2 for i in range(n)) ** 0.5

    if denominator_x == 0 or denominator_y == 0:
        raise ValueError("Standard deviation of one or both lists is zero.")

    return numerator / (denominator_x * denominator_y)

# Example usage
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

print(pearson_correlation(x, y))  # Output: 1.0
