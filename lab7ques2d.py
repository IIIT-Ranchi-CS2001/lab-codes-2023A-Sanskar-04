def plot_prime_and_composite_scatter(
    primes, prime_squares, composites, composite_sqrts
):
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Prime numbers vs squares
    axs[0].scatter(primes, prime_squares, color="blue", label="Primes")
    axs[0].set_title("Prime Numbers vs Their Squares")
    axs[0].set_xlabel("Prime Numbers")
    axs[0].set_ylabel("Squares")
    axs[0].legend()

    # Composite numbers vs square roots
    axs[1].scatter(composites, composite_sqrts, color="red", label="Composites")
    axs[1].set_title("Composite Numbers vs Their Square Roots")
    axs[1].set_xlabel("Composite Numbers")
    axs[1].set_ylabel("Square Roots")
    axs[1].legend()

    plt.tight_layout()
    plt.show()


# Call the plotting function
plot_prime_and_composite_scatter(primes, prime_squares, composites, composite_sqrts)
