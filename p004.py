# Largest palindrome product
# Problem 4 
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    for i in range(len(n)):
        if n[i] != n[len(n) - i - 1]:
            return False
    return True


def solution(minimum, maximum):
    largest = 0
    for i in range(minimum, maximum+1):
        for j in range(minimum, maximum+1):
            multi = i*j
            if is_palindrome(str(multi)) and multi > largest:
                largest = multi
    return largest


def main():
    minimum = 100
    maximum = 999
    ans = solution(minimum, maximum)
    print(ans)


if __name__ == "__main__":
    main()
