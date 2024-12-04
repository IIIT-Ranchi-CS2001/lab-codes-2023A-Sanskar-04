import random
import matplotlib.pyplot as plt


def generate_random_numbers(K, N):
    if K < 10:
        raise ValueError("K must be at least 10.")
    return [random.randint(1, N) for _ in range(K)]


# User inputs
K = int(input("Enter the number of random numbers to generate (minimum 10): "))
while K < 10:
    print("K must be at least 10.")
    K = int(input("Enter the number of random numbers to generate (minimum 10): "))
N = int(input("Enter the upper limit for random numbers: "))

# Generate random numbers and plot histogram
random_numbers = generate_random_numbers(K, N)
plt.hist(random_numbers, bins=10, color="skyblue", edgecolor="black")
plt.title("Distribution of Random Numbers")
plt.xlabel("Number Range")
plt.ylabel("Frequency")
plt.show()
