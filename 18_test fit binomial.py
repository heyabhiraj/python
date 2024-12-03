import numpy as np
from scipy.stats import binom, chisquare

def goodness_of_fit_binomial(data, n, p):
    """
    Test the goodness of fit of a dataset to a binomial distribution.

    Args:
        data (list): The observed data (number of successes in each trial).
        n (int): The number of trials.
        p (float): The probability of success on a single trial.

    Returns:
        dict: A dictionary with the chi-squared statistic, p-value, and conclusion.
    """
    # Calculate the observed frequencies
    observed_freqs = np.bincount(data, minlength=n+1)

    # Calculate the expected frequencies using the binomial distribution PMF
    expected_freqs = [binom.pmf(k, n, p) * len(data) for k in range(n+1)]

    # Perform Chi-squared goodness-of-fit test
    chi_stat, p_value = chisquare(observed_freqs, expected_freqs)

    # Conclusion based on p-value
    conclusion = (
        "Reject the null hypothesis (data does not fit the binomial distribution)"
        if p_value < 0.05
        else "Fail to reject the null hypothesis (data fits the binomial distribution)"
    )

    return {
        "chi_squared_statistic": chi_stat,
        "p_value": p_value,
        "conclusion": conclusion
    }

# Example usage
data = [3, 4, 2, 5, 3, 6, 2, 3, 4, 2, 4, 3, 5, 3, 4]  # Observed data (e.g., number of successes)
n = 6  # Number of trials
p = 0.5  # Probability of success in a single trial

result = goodness_of_fit_binomial(data, n, p)

# Print the result
print("""
chi_squared_statistic: {}
p_value: {}
conclusion: {}
""".format(result["chi_squared_statistic"], result["p_value"], result["conclusion"]))