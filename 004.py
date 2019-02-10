#!/usr/bin/env python3

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

largest = 0
min = 100
max = 999

for i in range(min, max):
    for j in range(min, max):
        multi = i*j
        if is_palindrome(str(multi)) and multi > largest:
            largest = multi

print(largest)
