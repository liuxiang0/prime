# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:33:29 2018
@author: Liu Xiang
@email : liuxiangxyd@163.com
filename: primes.py
class Prime(object)
including:
sample p = Prime(n)

Property: 
    p.prime = n 给定的正整数, p.flag 是否为素数？

Method：
bool is_prime(self) :     质数判断函数，True为质数，否则不是质数
bool MPLLtest(self,p):        Lucas_Lehmer_Test(p) 梅森素数2**p-1判断法，p为素数
def  number_of_digital(self):   计算超大正整数n的位数
     all_primes(self,start=2) :  大于start的质数无穷序列，generator of infinite primes list
     primes_between(self,start=2,end=5) : 得到[start,end]之间的质数序列，generator
     count_of_primes(self) : 小于n的质数个数（计数）
     primes_list(self) :  得到指定范围[lower, upper)内的所有质数列表List，开闭区间的所有质数列表
def sum_of_primes(self): 小于n的所有质数之和    

"""


class Prime(object):
    """    This is Prime class(素数 类的定义)    """

    def __init__(self, n):
        self._prime = n

    @property
    def prime(self):
        return self._prime

    def flag(self):
        self._flag = self.is_prime(self)
        return self._flag

    """                  
    @prime.setter
    def prime(self, value):
        self._prime = value
        
    @prime.deleter
    def prime(self):
        del self._prime
    """

    def is_prime(self):
        """
        素数判断函数，返回True时为质数，否则不是!
        不需要用math.sqrt()函数，改用乘方(**0.5)代替开方sqrt()，首先排除素数2和大于2的偶数
        don't use math.sqrt，at first delete even number
        """
        number = self._prime
        if number == 2:
            return True  # 唯一的偶数是素数
        if number < 2 or number % 2 == 0:
            return False  # 第一条语句已经清除了偶素数2，现在只要清除除2以外的偶数
        # 起始数是奇数3，间隔为偶数2，就是判断3以后的奇数是否为素数？奇数不可能有偶因子
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:  # Not number % i
                return False  # 只要能找到一个

        return True

        """ #def is_prime(number):
            # 如果用 平方 和 while 循环，参见下面：
            i = 3
            while i*i <= n:
                if n % i == 0:  return False
                i += 2    # 偶数已经排除了，只判断奇数。奇数不可能有偶因子
        """

    def MPLLtest(self, p):
        """
        判断 2**p-1是否为梅森素数Mersenne Prime，形如 2**p-1的素数，p为素数
        Lucas_Lehmer_Test(p)    
        """
        # Lucas_Lehmer_Test(p)
        # if not self.is_prime(self, p):
        #   raise ValueError

        s = 4
        M = 2 ** p - 1
        for i in range(2, p):  # repeat p-2 times
            s = (s * s - 2) % M

        if s == 0:
            return True  # 2**p-1 is prime
        else:
            return False  # 2**p -1 is composite

    def all_primes(self, start=2):
        """
        所有素数生成器prime generator，得到==无限循环==的质数序列，从start开始！
        """
        while True:
            tmp = Prime(start)
            if tmp.is_prime():
                yield start
            start += 1  # infinite loop

    def primes_between(self, start=2, end=5):
        """
        区间素数生成器，得到start与end之间[start,end]--闭区间 的质数序列！
        """
        s, e = start, end  # copy start,end to s,e 
        while s <= e:
            tmp = Prime(s)
            if tmp.is_prime():
                yield s
            s += 1

    def primes_list(self):
        """
        自动生成不大于_prime的素数序列
        """
        return self.primes_between(start=2, end=self._prime)

    def sum_of_primes(self):
        """
        得到不超过指定数MaxNum的所有质数之和。sum of all primes which is less than MaxNum 
        """
        maxium = self._prime
        if maxium < 2:
            return 0

        total = 2
        for nextPrime in self.primes_between(3, maxium):
            total += nextPrime  # sum(2+3+5+7+... +lastPrime < MaxNum)

        return total

    def count_of_primes(self):
        """
        利用优化的质数判断函数is_prime(), 得到小于upper的质数个数
        get prime count which less than the given upper
        """
        upper = self._prime
        if upper < 2:
            return 0
        primeCount = 0  # 初始计数为 0        
        for n in range(2, upper):
            tmp = Prime(n)
            if tmp.is_prime():
                primeCount += 1

        return primeCount

    def number_of_digital(self):
        """
        digital_number(n): 获取一个正整数的数字个数
        原理： 10**(d-1) <= n < 10**d, 表明n有 d个数字
        换算成log10， 得到 d-1 <= log(n) < d, log(n)< d <= log(n)+1
        """
        from math import log10 as log

        n = self._prime
        if n <= 0:  # 排除负数和零，实际上可以产生一个ValueError
            return 1
        else:
            return int(log(n)) + 1


if __name__ == '__main__':

    p = Prime(700)
    print("Number %d is Prime? Answer is %s " % (p.prime, p.is_prime()))
    print("Count of Primes(<=%d) = %d " % (p.prime, p.count_of_primes()))
    print("Sum of Primes(<=%d) = %d " % (p.prime, p.sum_of_primes()))
    print("List of Primes(<=%d): %s" % (p.prime, list(p.primes_list())))
    for tp in p.primes_list():
        if p.MPLLtest(tp):
            print("MP 2^%d-1 = %d is prime" % (tp, 2 ** tp - 1))
