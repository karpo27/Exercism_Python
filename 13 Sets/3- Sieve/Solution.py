def primes(limit):
    primes_list = []
    for i in range(2, limit + 1):
        c = 0
        number = 2
        while number <= i:
            if i % number == 0:
                c += 1
                number += 1
            else:
                number += 1

        if c == 1:
            primes_list.append(i)

    return primes_list
    
