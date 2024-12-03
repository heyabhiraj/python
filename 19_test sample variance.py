from scipy.stats import f
import numpy as np

def test_variance_significance(sample1, sample2, alpha=0.05):
    """
    Test the significance of the difference between the variances of two samples using an F-test.

    Args:
        sample1 (list): First sample of numbers.
        sample2 (list): Second sample of numbers.
        alpha (float): Significance level (default is 0.05).

    Returns:
        dict: A dictionary with the F-statistic, p-value, and conclusion.
    """
    if len(sample1) < 2 or len(sample2) < 2:
        raise ValueError("Both samples must have at least two elements.")
    
    # Calculate the sample variances
    var1 = np.var(sample1, ddof=1)
    var2 = np.var(sample2, ddof=1)
    
    # Sample sizes
    n1 = len(sample1)
    n2 = len(sample2)
    
    # Calculate the F-statistic (larger variance / smaller variance)
    f_stat = var1 / var2 if var1 >= var2 else var2 / var1
    
    # Degrees of freedom
    df1 = n1 - 1
    df2 = n2 - 1
    
    # Calculate the p-value using the F-distribution
    p_value = 2 * min(f.cdf(f_stat, df1, df2), 1 - f.cdf(f_stat, df1, df2))
    
    # Conclusion based on p-value
    conclusion = (
        "Reject the null hypothesis (significant difference in variances)"
        if p_value < alpha
        else "Fail to reject the null hypothesis (no significant difference in variances)"
    )
    
    return {
        "f_statistic": f_stat,
        "p_value": p_value,
        "conclusion": conclusion
    }

# Example usage
sample1 = [12, 14, 16, 18, 20]
sample2 = [22, 24, 26, 28, 30]

result = test_variance_significance(sample1, sample2)

# Print the result
print("""
f_statistic: {}
p_value: {}
conclusion: {}
""".format(result["f_statistic"], result["p_value"], result["conclusion"]))