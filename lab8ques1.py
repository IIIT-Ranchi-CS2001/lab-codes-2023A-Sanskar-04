import numpy as np

# Step 1: User inputs for dimensions
shape1 = tuple(
    map(int, input("Enter the shape for the first 3D array (e.g., 3 3 3): ").split())
)
shape2 = tuple(
    map(int, input("Enter the shape for the second 3D array (e.g., 3 3 3): ").split())
)

# Step 2: Generate random elements for A1 and A2
A1 = np.random.randint(1, 101, size=shape1)  # Random numbers between 1 and 100
A2 = np.random.randint(1, 101, size=shape2)  # Random numbers between 1 and 100

print("First 3D Array (A1):\n", A1)
print("Second 3D Array (A2):\n", A2)

# Step 3: Select elements divisible by 5 from A1
div_by_5 = A1[A1 % 5 == 0]
print("\nElements of A1 divisible by 5:\n", div_by_5)

# Step 4: Select elements divisible by 4 from A2
div_by_4 = A2[A2 % 4 == 0]
print("\nElements of A2 divisible by 4:\n", div_by_4)

# Step 5: Join the two arrays into a single-dimensional array
combined_array = np.concatenate((div_by_5, div_by_4))
print("\nCombined Array:\n", combined_array)

# Step 6: Construct the largest possible square matrix
n = int(
    np.floor(np.sqrt(combined_array.size))
)  # Determine the size of the square matrix
largest_square_matrix = combined_array[: n * n].reshape(n, n)

print("\nLargest Possible Square Matrix:\n", largest_square_matrix)
