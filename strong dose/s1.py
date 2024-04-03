# declaring a set, for storing unique prime factors
def prime_factors_count(n):
    factors = set()
    i = 2
# loop for finding the prime factors of a number
# if 'i' is divisible by 'n' then the number isn't prime
# i*i<=n : checking this condition as we need not check all 'i' below 'n' it is enough to check till n/2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)

    return len(factors)


# finding four numbers with 4 distinct prime numbers
def consecutive_ints_with_four_prime_factors():
    consecutive_integers = []
    num = 1
# running the loop until we get 4 distinct primes, if yes then adding to list else resetting list
    while len(consecutive_integers) < 4:
        if prime_factors_count(num) == 4:
            consecutive_integers.append(num)
        else:
            consecutive_integers = []
        num += 1
    return consecutive_integers


# finding and printing the first four consecutive number with 4 distinct primes
first_four_consecutive = consecutive_ints_with_four_prime_factors()
print("The first four consecutive integers with four distinct prime factors each are:", first_four_consecutive)
