#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:33:29 2018
@author: Liu Xiang
@email : liuxiangxyd@163.com
filename: primespy.py
including:
def  number_of_digital(self): 计算超大正整数n的位数

Functions:
bool is_prime(p) :  质数判断函数，True为质数，否则不是质数
bool MPLLtest(p): Lucas_Lehmer_Test(p) 梅森素数2**p-1判断法，p为素数
genrator primes_generator(start=2, limit=float("inf")): generate infinite primes
"""


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
    """List all primes below n

    """
    pl = primes_generator(2, n)
    if filename is None:
        print("Primes list (less than {p}) is below.".format(p=n))
        print(list(pl))
    else:
        with open(filename,'w') as outf:
            outf.write("Primes list (less than {p}) is below.\n".format(p=n))
            outf.write(str(list(pl)))
            outf.close()

def primes_start(start, n, filename=None): 
    """List of prime numbers from start up to n.

    """
    pl = primes_generator(start, n)
    if filename is None:
        print("Primes list [{s},{e}).".format(s=start, e=n))
        print(list(pl))
    else:
        with open(filename,'w') as outf:
            outf.write("Primes list [{s},{e}).\n".format(s=start, e=n))
            outf.write(str(list(pl)))
            outf.close()

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
    nth = abs(n)
    

def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    #a[2] = True
    for n in range(4, limit, 2):
        a[n] = False
    root_limit = int(limit**.5)+1
    for i in range(3, root_limit):
        if a[i]:
            for n in range(i*i, limit, 2*i):
                a[n] = False
    return a

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
    max_p = 1000000
    output_file = 'primes_list' + str(max_p) + '.txt'

    primes(max_p, filename=output_file)

    '''
    p = primes_generator(2, max_p)
    pList = list(p)  # after list(p), p is None
    MPlist=[]
    for v in pList:
        if is_mersenne(v):
            MPlist.append(v)
        #print("Mersenne 2**{val}-1 is prime? {Bool}".format(val=v, Bool=MPLLtest(v)))
    
    sum_primes = sum(pList)
    count_primes = len(pList)
    print("sum of primes is {s}, count of primes is {c}".format(s=sum_primes, c=count_primes))
    
    with open(output_file, mode='a') as fw:
        fw.write("Mersenne prime list: 2^p-1, where p include the following primes list \n")
        fw.write(str(MPlist)+'\n')
        fw.write("primes less than " + str(max_p)+'\\')
        fw.write("sum is " + str(sum_primes)+'\\')
        fw.write("count is " + str(count_primes)+'\\')
        fw.write("primes percentage(%): " + str(count_primes/max_p*100)+'\n\n')
        fw.close()
    '''