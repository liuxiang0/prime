#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
# Program to check Armstrong numbers in certain interval
Arstrong number of oder n just like
$abcd=a^n+b^n+c^n+d^n, where n = len(str(abcd))$
e.g 153=1^3+5^3+3^3
Result: 100=10**2-->1000000=10**6
Armstrong 153, order 3
Armstrong 370, order 3
Armstrong 371, order 3
Armstrong 407, order 3
Armstrong 1634, order 4
Armstrong 8208, order 4
Armstrong 9474, order 4
Armstrong 54748, order 5
Armstrong 92727, order 5
Armstrong 93084, order 5
Armstrong 548834, order 6
"""
lower = 100
upper = 1000000

# To take input from the user
# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    # order of number
    order = len(str(num))
    # initialize sum
    sum = 0

    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print("Armstrong {arm}, order {n}".format(arm=num, n=order))