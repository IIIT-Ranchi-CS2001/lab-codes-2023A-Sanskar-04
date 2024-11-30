import numpy as np


def Create_Array(*args):

    # Create a square array with diagonal elements from the arguments
    n = len(args)
    array = np.zeros((n, n), dtype=int)
    np.fill_diagonal(array, args)
    return array


# Example usage
result = Create_Array(1, 2, 3, 4)
print(result)
