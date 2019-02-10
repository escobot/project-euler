#!/usr/bin/env python3

# Smallest multiple
# Problem 5 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def modular_sum(count):
    mods = list(range(11,20)) #11-19
    sum = 0
    for n in mods:
        sum = sum + count%n
    return sum


smallest = 0
found = False
count = 0

while found == False:
    count = count + 20 #reduce search list
    if modular_sum(count) == 0:
        smallest = count
        found = True

print(count)