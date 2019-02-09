#!/usr/bin/env python3

# Multiples of 3 and 5
# Problem 1 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000

max = 1000
sum = 0

for x in range(1,max):
    if x % 3 == 0:
        sum = sum + x
    elif x % 5 == 0:
        sum = sum + x

print(sum)