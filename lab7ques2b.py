def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def separate_prime_and_composite(numbers):
    primes = [num for num in numbers if is_prime(num)]
    composites = [num for num in numbers if num > 1 and not is_prime(num)]
    return primes, composites


# Separate and visualize primes and composites
primes, composites = separate_prime_and_composite(random_numbers)

categories = ["Primes", "Composites"]
counts = [len(primes), len(composites)]
plt.bar(categories, counts, color=["blue", "red"])
plt.title("Count of Primes vs Composites")
plt.ylabel("Count")
plt.show()
