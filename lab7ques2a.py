import math


def compute_square_and_sqrt(primes, composites):
    prime_squares = [num**2 for num in primes]
    composite_sqrts = [math.sqrt(num) for num in composites]
    return prime_squares, composite_sqrts


prime_squares, composite_sqrts = compute_square_and_sqrt(primes, composites)

# Scatter plots for transformations
plt.scatter(primes, prime_squares, color="blue", label="Prime Squares")
plt.scatter(composites, composite_sqrts, color="red", label="Composite Square Roots")
plt.title("Transformations: Prime Squares and Composite Square Roots")
plt.xlabel("Original Numbers")
plt.ylabel("Transformed Values")
plt.legend()
plt.show()
