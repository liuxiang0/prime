# prime class
Created on Sat May 12 21:33:29 2018
@author: Liu Xiang
@email : liuxiangxyd@163.com
filename: Primes.py
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