def list_primes(n):
    """List all prime numbers up to n"""
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

if __name__ == "__main__":
    print("Prime numbers up to 100:")
    primes = list_primes(100)
    print(primes)
    print(f"\nTotal prime numbers up to 100: {len(primes)}")
