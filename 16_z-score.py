def calculate_z_scores(data):
    """
    Calculate the Z-scores for a list of numbers.

    Args:
        data (list): List of numerical values.

    Returns:
        list: List of Z-scores corresponding to the input values.
    """
    if not data:
        raise ValueError("The input list must not be empty.")
    
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5

    if std_dev == 0:
        raise ValueError("Standard deviation is zero, Z-scores cannot be calculated.")

    z_scores = [(x - mean) / std_dev for x in data]
    return z_scores

# Example usage
data = [10, 20, 30, 40, 50]
z_scores = calculate_z_scores(data)
print("Z-scores:", z_scores)
