import numpy as np


shape1 = tuple(
    map(int, input("Enter the shape for the first 3D array (e.g., 3 3 3): ").split())
)
shape2 = tuple(
    map(int, input("Enter the shape for the second 3D array (e.g., 3 3 3): ").split())
)


A1 = np.random.randint(1, 101, size=shape1)
A2 = np.random.randint(1, 101, size=shape2)

print("First 3D Array (A1):\n", A1)
print("Second 3D Array (A2):\n", A2)
div_by_5 = A1[A1 % 5 == 0]
print("\nElements of A1 divisible by 5:\n", div_by_5)
div_by_4 = A2[A2 % 4 == 0]
print("\nElements of A2 divisible by 4:\n", div_by_4)

combined_array = np.concatenate((div_by_5, div_by_4))
print("\nCombined Array:\n", combined_array)

n = int(np.floor(np.sqrt(combined_array.size)))
largest_square_matrix = combined_array[: n * n].reshape(n, n)

print("\nLargest Possible Square Matrix:\n", largest_square_matrix)
