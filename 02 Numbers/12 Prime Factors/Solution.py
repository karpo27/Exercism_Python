def divide(next_prime, value):
    for i in range(next_prime, value + 1):
        if value % i == 0:
            return i


def factors(value):
    if value <= 1:
        return []

    next_prime = 2
    primes = []
    while value > 1:
        next_prime = divide(next_prime, value)
        value = int(value / next_prime)
        primes.append(next_prime)

    return primes
