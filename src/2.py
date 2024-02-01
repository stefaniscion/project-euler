def even_fibonacci_sum(max):
    sum = 0
    a = 1
    b = 2
    while b < max:
        if b % 2 == 0:
            sum += b
        a, b = b, a + b
    return sum


print(even_fibonacci_sum(4000000))
