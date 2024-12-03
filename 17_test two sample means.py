from scipy.stats import ttest_ind
"""Test the significance of the difference between two sample means.

    Args:
        sample1 (list): First sample of numbers.
        sample2 (list): Second sample of numbers.
        test_type (str): Type of test to perform ("independent" or "paired").
        alpha (float): Significance level (default is 0.05).

    Returns:
        dict: A dictionary containing the t-statistic, p-value, and conclusion."""
def test_sample_means(sample1, sample2, alpha=0.05):
    if not sample1 or not sample2:
        raise ValueError("Both samples must contain data.")

    # Perform a two-sample t-test
    t_stat, p_value = ttest_ind(sample1, sample2)

    # Conclusion based on the p-value and significance level
    conclusion = "Reject the null hypothesis (means are significantly different)" if p_value < alpha else "Fail to reject the null hypothesis (no significant difference in means)"

    return {
        "t_statistic": t_stat,
        "p_value": p_value,
        " conclusion": conclusion
    }

# Example usage
sample1 = [12, 14, 16, 18, 20]
sample2 = [22, 24, 26, 28, 30]

result = test_sample_means(sample1, sample2)
print(result)
