#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:33:29 2019
Modified on Wed April 24 14:01 2019
@author: Liu Xiang
@email : liuxiangxyd@163.com
filename: primespy.py
including:
def  number_of_digital(self): 计算超大正整数n的位数

Functions:
bool is_prime(p) :  质数判断函数，True为质数，否则不是质数
bool MPLLtest(p): Lucas_Lehmer_Test(p) 梅森素数2**p-1判断法，p为素数
genrator primes_generator(start=2, limit=float("inf")): generate infinite primes

References:
1. [The first fifty million primes][https://primes.utm.edu/lists/small/millions/]
2. [The fastest way to list all primes below n][https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3638617#3638617]
3. 
Comparisons with:
import primesieve   (1)
primes = primesieve.generate_primes(10**8)

from sympy import sieve  (2)
primes = list(sieve.primerange(1, 10**6))

"""


import time
import numpy
import itertools
import numpy as np
from itertools import compress

izip = itertools.zip_longest
chain = itertools.chain.from_iterable
compress = itertools.compress


def rwh_primes2(n):
    correction = (n%6 > 1)
    n = {0:n, 1:n-1,2:n+4, 3:n+3, 4:n+2, 5:n+1}[n%6]
    sieve = [True] * (n//3)
    sieve[0] = False
    for i in range(int(n**0.5)//3 + 1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)//3)      ::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
        sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1, n//3-correction) if sieve[i]]


def rwh_primes2_python3(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    zero = bytearray([False])
    size = n//3 + (n % 6 == 2)
    sieve = bytearray([True]) * size
    sieve[0] = False
    for i in range(int(n**0.5)//3 + 1):
      if sieve[i]:
        k=3*i + 1 | 1
        start = (k*k + 4*k - 2*k*(i&1))//3
        sieve[(k*k)//3::2*k]=zero*((size - (k*k)//3 - 1) // (2*k) + 1)
        sieve[  start ::2*k]=zero*((size -   start -  1) // (2*k) + 1)
    ans = [2, 3]
    poss = chain(izip(*[range(i, n, 6) for i in (1, 5)]))
    ans.extend(compress(poss, sieve))
    return ans


def number_of_digital(any_integer):
    """
    digital_number(n): 获取一个正整数的数字个数
    原理： 10**(d-1) <= n < 10**d, 表明n有 d个数字
    换算成log10， 得到 d-1 <= log(n) < d, log(n)< d <= log(n)+1
    """
    from math import log10 as log

    # return (int(log(n))+1 if n > 0 else 0)
    n = abs(any_integer)
    if not n:  # 排除负数和零，实际上可以产生一个ValueError
        return 1
    return int(log(n)) + 1


def is_mersenne(p):
    """
    input: any one prime
    output: True if 2**p-1 is prime else False
    判断 2**p-1是否为梅森素数Mersenne Prime，形如 2**p-1的素数，p为素数
    Lucas_Lehmer_Test(p)    
    """
    # Lucas_Lehmer_Test(p)
    # if not self.is_prime(self, p):
    #   raise ValueError

    s = 4
    M = 2 ** p - 1
    for _ in range(2, p):  # repeat p-2 times
        s = (s * s - 2) % M

    return not s
    # True: 2**p-1 is prime
    # False: 2**p -1 is composite


def primes_generator(start=2, limit=float("inf")):
    """
    input: given the first prime
    output: generate the infinite primes with yield
    所有素数生成器prime generator，得到==无限循环==的质数序列，从start开始！
    include 区间素数生成器，得到start与limit之间[start,limit)--闭区间 的质数序列！
    """
    s = start  # start variable will not changed
    while True and s < limit:
        if is_prime(s):
            yield s
        s += 1  # infinite loop


def is_prime(N):
    """
    Input: any integer which is greater than 1.
    Output: bool True represent integer is prime number.
    素数判断函数，返回True时为质数，否则不是!
    不需要用math.sqrt()函数，改用乘方(**0.5)代替开方sqrt()，
    首先排除素数2和大于2的偶数
    don't use math.sqrt，at first skip all even number except 2
    """
    number = abs(N)
    if number%2 == 0:
        return (number==2)  # 唯一的偶数2,-2是素数
    if number%3 == 0:
        return (number==3)  # 第一条语句已经清除了偶素数2，现在只要清除除2以外的偶数
    # 起始数是奇数3，间隔为偶数2，就是判断3以后的奇数是否为素数？奇数不可能有偶因子
    if number%5 == 0:
        return (number==5)
    if number%7 == 0:
        return (number==7)
    # upper = int(number ** 0.5)+1  # only one operation sqrt()
    i = 11
    while i*i <= number:  # for i in range(11, upper, 2):
        if not (number % i):  # replace number % i == 0:
            return False  # 只要能找到一个
        i += 2

    return True


def primes(n, filename=None):
    """List all primes below n"""

    pl = primes_generator(2, n)
    if filename is None:
        print("Primes list (less than {p}) is below.".format(p=n))
        print(list(pl))
    else:
        with open(filename,'w') as outf:
            outf.write("Primes list (less than {p}) is below.\n".format(p=n))
            outf.write(str(list(pl)))
            outf.close()
    return 

def primes_start(start, n, filename=None): 
    """List of prime numbers from start up to n."""

    pl = primes_generator(start, n)
    if filename is None:
        print("Primes list [{s},{e}).".format(s=start, e=n))
        result = list(pl)
        print(result)
    else:
        with open(filename,'w') as outf:
            outf.write("Primes list [{s},{e}).\n".format(s=start, e=n))
            result = list(pl)
            outf.write(str(result))
            outf.close()
    
    return result


def primes_sum_count(n):
    """The summation of prime numbers from 2 up to n, 
    and count of prime numbers. 
    The optimal number of threads will be determined 
    for the given number and system.
    """
    pl = list(primes_generator(2, n))
    return sum(pl), len(pl)


def primes_sum_count_start(start, n):
    """The summation of prime numbers from start up to n,
    and count of prime numbers. 
    The optimal number of threads will be determined 
    for the given numbers and system.
    """
    pl = list(primes_generator(start, n))
    return sum(pl), len(pl)


def primes_nth(n):
    """The nth prime number.
    """
    pl = primes_generator(2)
    for _ in range(n-1):
        next(pl)
    return(next(pl))
    
# Several sieve algorithms for fingding primes list

def primes_sieve1(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for n in range(4, limit, 2):
        a[n] = False  # all even number >=4
    root_limit = int(limit**.5)+1
    for i in range(3, root_limit):
        if a[i]:
            a[i*i::2*i] = False  # i*(i+1) is even
            #for n in range(i*i, limit, 2*i):
            #    a[n] = False
    return [i for i in range(limit) if a[i]]


def primes_sieve2(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    upper = int(n**0.5)+1
    for i in range(3, upper, 2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def primes_sieve3(n):
    """ Returns  a list of primes < n """
    # begin half-sieve
    sieve = [True] * (n>>1)
    upper = int(n**0.5)+1
    for i in range(3, upper, 2):
        if sieve[i>>1]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


def primes_npsieve1(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n//2, dtype=numpy.bool)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1


def primes_npsieve2(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1, int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]


def primes_npsieve3a(upto):
    """It sieves a Boolean array referring to its indices only and 
    elicits prime numbers from the indices of all True values. 
    No module needed.
    """
    mat = np.ones((upto), dtype=bool)  # initial all postion True
    mat[0] = mat[1] = 0
    mat[4::2] = 0  # let all even (>4) position is False

    upper = int(upto ** 0.5)
    for idx in range(3, upper + 1, 2):
        mat[idx*idx::idx] = 0  # reject the idx's multiple
    return np.where(mat == 1)[0]


def primes_npsieve3b(upto):
    """It sieves a Boolean array referring to its indices only and 
    elicits prime numbers from the indices of all True values. 
    No module needed.
    """
    mat = np.ones((upto), dtype=bool)  # initial all postion True
    mat[0] = mat[1] = 0
    # mat[4::2] = 0  # first delete all even number except 2
    upper = int(upto ** 0.5)

    small_primes = [2, 3, 5, 7]  # , 11, 13, 17, 19]  # ,23]
    for p in small_primes:
        mat[p*p::p] = 0  # let all multiple of a prime (>=4) position is False
    
    for idx in range(11, upper + 1, 2):
        mat[idx*idx::idx] = 0  # reject the idx's multiple
    return np.where(mat == 1)[0]


def primes_npsieve6(upto):
    """This is one of the best algorithm"""

    # replace //2 for >>1, shift one bit
    primes=np.arange(3, upto+1, 2)  # odd series below upto
    # primes[k] = 2k+3, k=0,1,2,3,... k is index
    # k = (primes-3)//2
    isprime=np.ones((upto-1)>>1, dtype=bool)  # inital 1
    upper = int(upto**0.5)
    for factor in primes[:upper]:
        if isprime[(factor-3)>>1]:  # equavilent to (factor-2)//2 
            #isprime[int((factor*3-2)/2):int((upto-1)/2):factor]=0
            # because factor=2k+3, so (factor-3)//2+factor
            isprime[3*((factor-1)>>1)::factor]=0
            # a*b//2=(a*b)//2 not equal to a*(b//2), eg 5*7//2!=5*(7//2)

    return np.insert(primes[isprime], 0, 2)
    # np.insert statement cannot run under >>> command line


from bitarray import bitarray
def primes_to(n):
    """
    python -m timeit -n10 -s "import euler" "euler.primes_to(1000000000)"
    10 loops, best of 3: 46.5 sec per loop
    """
    size = n//2
    sieve = bitarray(size)
    sieve.setall(1)
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            sieve[(i+i*val)::val] = 0
    return [2] + [2*i+1 for i, v in enumerate(sieve) if v and i > 0]


def rwh_primes1v1(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2, *compress(range(3, n, 2), sieve[1:])]

def rwh_primes1v2(n):
    """ Returns a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2+1)
    for i in range(1, int(n**0.5)//2 + 1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


def primes_sundaram3(max_n):
    numbers = list(range(3, max_n+1, 2))
    half = (max_n)//2
    initial = 4

    for step in range(3, max_n+1, 2):
        for i in range(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)


def human_format(num):
    # https://stackoverflow.com/questions/579310/formatting-long-numbers-as-strings-in-python?answertab=active#tab-top
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

def is_prime_bakup(number):
    """ 如果用 平方 和 while 循环，参见下面：
    """
    n = abs(number)
    if n%2==0:
        return n==2

    i = 3
    while i*i <= n:
        if not (n % i):  # replace n % i == 0:  
            return False
        i += 2    # 偶数已经排除了，只判断奇数。奇数不可能有偶因子
    return True


if __name__ == '__main__':
    pass
