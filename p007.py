# 10001st prime
# Problem 7 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# as of solving this challenge the largest prime number known is 24,862,048


def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def solution(nth):
    count = 1
    prime = 0
    while prime != nth:
        count = count + 1  # primes start at 2
        if is_prime(count):
            prime = prime + 1
    return count


def main():
    ans = solution(10001)
    print(ans)


if __name__ == '__main__':
    main()

