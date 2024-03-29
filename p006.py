# Sum square difference
# Problem 6 
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the 
# first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.

def solution(limit):
    sum_of_squares = 0
    square_of_sums = 0

    for i in range(1, limit+1):
        sum_of_squares = sum_of_squares + i*i
        square_of_sums = square_of_sums + i
    square_of_sums = square_of_sums * square_of_sums
    return square_of_sums - sum_of_squares


def main():
    ans = solution(100)
    print(ans)


if __name__ == '__main__':
    main()
