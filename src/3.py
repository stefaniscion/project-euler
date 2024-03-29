def smallest_divisor(n):
    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1


def largest_prime_factor(n):
    largest_prime_factor = None
    while n > 1:
        factor = smallest_divisor(n)
        if largest_prime_factor is None or largest_prime_factor < factor:
            largest_prime_factor = factor
        n = n / factor
    return largest_prime_factor


print(largest_prime_factor(600851475143))
