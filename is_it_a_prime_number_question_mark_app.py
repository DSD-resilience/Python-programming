def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # exclude all other even numbers
    
    for i in range(3, int(n ** 0.5) + 1, 2):  # check only odd divisors up to sqrt(n)
        if n % i == 0:
            return False
    return True
