#!/usr/bin/env python3

# Summation of primes
# Problem 10 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def is_prime(n):
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i = i + 1
    return True

sum, finished, n = 2, False, 3

while finished == False:
    if is_prime(n):
        print(n)
        if n < 2000000:
            sum = sum + n
        else:
            finished = True
    n = n + 2

print(sum)