def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')

    primes = 0
    for i in range(2, 200000):
        counter = 0
        for j in range(2, int(i/2) + 1):
            if i % j == 0:
                counter += 1
                break
        if counter == 0:
            primes += 1
        if primes >= number:
            return i
            
