# Multiples of 3 and 5
# Problem 1 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000


def solution(limit):
    s = 0
    for x in range(1, limit):
        if x % 3 == 0:
            s = s + x
        elif x % 5 == 0:
            s = s + x
    return s


def main():
    limit = 1000
    ans = solution(limit)
    print(ans)


if __name__ == "__main__":
    main()
