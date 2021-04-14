# Smallest multiple
# Problem 5 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def modular_sum(count, limit):
    minimum = int(limit / 2) + 1
    mods = list(range(minimum, limit))  # 11-19
    s = 0
    for n in mods:
        s = s + count % n
    return s


def solution(limit):
    found = False
    count = 0

    while not found:
        count = count + limit
        if modular_sum(count, limit) == 0:
            found = True
    return count


def main():
    ans = solution(10)
    print(ans)


if __name__ == '__main__':
    main()
