# Fastest way to list all primes up to N

Created on Sat May 12 21:33:29 2018  
reviewed by: Liu Xiang  
@email: liuxiangxyd@163.com  
filename: pyprimes.py

## **Functions**

pyprimes module provides the following functions:

1. `primes(n, filename=None)`: List of prime numbers from 2 up to n.
2. `primes_between(start, n, filename=None)`: List of prime numbers from start up to n.
3. `primes_sum_count(n)`: The summation of prime numbers from 2 up to n. The optimal number of threads will be determined for the given number and system.
4. `primes_sum_count_between(start, n)`: The summation of prime numbers from start up to n. The optimal number of threads will be determined for the given numbers and system.
5. `primes_nth(n)`: Find the n-th prime.
6. `prime_n(n)`: List the first 'n' primes >= 2   
7. `factorize(n)`: List of tuples in the form of (prime, power) for the prime factorization of n.
8. `bool is_prime(N)`: prime detection.
9. `bool is_mersenne(p)`: Mersenne prime detection,  Lucas_Lehmer_Test(p) 梅森素数2**p-1判断法，p为素数.
10. `iteration primes_generator(start=2, limit=float("inf"))`: Primes generator, iterate all primes between start and limit.


**Method：**
~~~python
def  number_of_digital(self) :   计算超大正整数n的位数  
     all_primes(self,start=2) :  大于start的质数无穷序列，generator of infinite primes list  
     primes_between(self,start=2,end=5) : 得到[start,end]之间的质数序列，generator  
     count_of_primes(self) : 小于n的质数个数（计数）  
     primes_list(self) :  得到指定范围[lower, upper)内的所有质数列表List，开闭区间的所有质数列表  
     
def sum_of_primes(self): 小于n的所有质数之和
~~~

## SymPy

**SymPy** is another choice. It is a Python library for symbolic mathematics. It provides several functions for prime.

Functions |Descriptions
----------|------------
isprime(n)  |# Test if n is a prime number (True) or not (False).
primerange(a, b)  |# Generate a list of all prime numbers in the range [a, b).
randprime(a, b)  |# Return a random prime number in the range [a, b).
primepi(n)  |# Return the number of prime numbers less than or equal to n.
prime(nth)  |# Return the nth prime, with the primes indexed as prime(1) = 2. The nth prime is approximately n*log(n) and can never be larger than 2**n.
prevprime(n, ith=1)  |# Return the largest prime smaller than n
nextprime(n)  |# Return the ith prime greater than n
sieve.primerange(a, b)  |# Generate all prime numbers in the range [a, b), implemented as a dynamically growing sieve of Eratosthenes. 

## [Examples][2]

~~~python
    >>> from primesieve import *

    # Generate a list of the primes below 40
    >>> generate_primes(40)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    # Generate a list of the primes between 100 and 120
    >>> generate_primes(100, 120)
    [101, 103, 107, 109, 113]

    # Generate a list of the first 10 primes
    >>> generate_n_primes(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Generate a list of the first 10 starting at 1000
    >>> generate_n_primes(10, 1000)
    [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061]

    # Get the 10th prime
    >>> nth_prime(10)
    29

    # Count the primes below 10**9
    >>> count_primes(10**9)
    50847534
~~~

[More information reference][1]

[1]:https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/33356284#33356284
[2]:https://stackoverflow.com/questions/13326673/is-there-a-python-library-to-list-primes
[3]:https://primes.utm.edu/