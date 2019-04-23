# Fastest way to list all primes below N
Created on Sat May 12 21:33:29 2018
reviewed by: Liu Xiang
@email: liuxiangxyd@163.com
filename: primespy.py

Functions

1. primes(n, filename=None): List of prime numbers from 2 up to n.

2. primes_start(start, n, filename=None): List of prime numbers from start up to n.

3. primes_sum_count(n): The summation of prime numbers from 2 up to n. The optimal number of threads will be determined for the given number and system.

4. primes_sum_count_start(start, n): The summation of prime numbers from start up to n. The optimal number of threads will be determined for the given numbers and system.

5. primes_nth(n): The nth prime number.

6. factorize(n): List of tuples in the form of (prime, power) for the prime factorization of n.

including:
1. general judge way: bool is_prime(N)  # prime detection
2. Mersenne prime: bool is_mersenne(p)  # Lucas_Lehmer_Test(p) 梅森素数2**p-1判断法，p为素数
3. generator for primes: primes_generator(start=2, limit=float("inf"))
Property:
    p.prime = n 给定的正整数, p.flag 是否为素数？

Method：
def  number_of_digital(self):   计算超大正整数n的位数
     all_primes(self,start=2) :  大于start的质数无穷序列，generator of infinite primes list
     primes_between(self,start=2,end=5) : 得到[start,end]之间的质数序列，generator
     count_of_primes(self) : 小于n的质数个数（计数）
     primes_list(self) :  得到指定范围[lower, upper)内的所有质数列表List，开闭区间的所有质数列表
def sum_of_primes(self): 小于n的所有质数之和

[More information reference][1]

[1]:https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/33356284#33356284