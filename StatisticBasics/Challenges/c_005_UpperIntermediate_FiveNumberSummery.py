"""
c_005_UpperIntermediate_FiveNumberSummery

Five-number Summary
Write a function to return min, Q1, median, Q3, max for a given dataset using numpy.percentile().
"""
import random
import numpy as np
import pandas as pd

lstNums = list(random.sample(range(1, 20), 5))
print(f"List: {lstNums}")

def listStats(lst: list[int]) -> pd.DataFrame:
    """
    Return a pandas.DataFrame with min, Q1, median, Q3, max for a given
    list with integer values using numpy.percentile().

    :param lst: List with integer values.
    :return: pandas.DataFrame with statistic information
    """
    assert isinstance(lst, list), "Parameter must be a list"
    assert len(lst) > 0, "List must contain values"
    assert all(isinstance(x, int) for x in lst), "All list entries must be integers"

    stats = {
        "Min (Q0)": np.percentile(lst, 0),
        "Q1 (25%)": np.percentile(lst, 25),
        "Median (Q2)": np.percentile(lst, 50),
        "Q3 (75%)": np.percentile(lst, 75),
        "Max (Q4)": np.percentile(lst, 100)
    }

    return pd.DataFrame(stats, index=["Value"]).T

print(listStats(lstNums))