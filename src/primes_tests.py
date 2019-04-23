# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:33:11 2018

@author: liu xiang
Test Prime Package

"""
from primespy import primes_generator, is_mersenne, number_of_digital
from primespy import primes_sieve
import time
from  os import path as osp


def test_primes_sieve():
    LIMIT = 10**6
    s = time.time()
    primes = primes_sieve(LIMIT)
    plist=[i for i, x in enumerate(primes) if x]
    print("Elapsed(s): {T}.".format(T=time.time() - s))
    print(plist)
    print("Count is {C}, Sum is {S}.".format(C=len(plist), S=sum(plist)))

def test_primes_generator():
    if not osp.exists('mesernneprime.txt') :
        outfile = open('mesernneprime.txt','w')
    else:
        outfile = open('mesernneprime.txt','a')
        
    primes_max = 5000
    # if n =4000, elasped time = 49seconds in my notebook ThinkPad E450
    primes_gen = primes_generator(limit = primes_max)  # get prime list between [2,4000]
    primelist = list(primes_gen) # change iteration to list
    # print the above prime list 
    print( primelist)
    # start time for running
    start = time.time()

    outfile.write("Testing, time = %s \n" % time.strftime("%Y-%m-%d %H:%M:%S"))
    for pm in primelist:  # every i is prime
        if is_mersenne(pm):  # Mesernne Prime Testing by Lucas_Lehmer_Test
            mp = 2**pm -1
            outfile.write("DC={d}, MP=2^{p}-1={mp} \n".format(
                d = number_of_digital(mp), p=pm, mp=mp)
                )
            print("MP=2^{p}-1={m} is Mersenne Prime!\n".format(
                p=pm, m=2**pm-1)
                )
    
    outfile.write("Finished, time = %s \n" % time.strftime("%Y-%m-%d %H:%M:%S"))
    outfile.write("Finished, elasped(s): %d. \n " % (time.time()-start))
    
    outfile.close()


# test data        
if __name__ == '__main__':
    test_primes_sieve()
    test_primes_generator
    """
    if sys.argv[1].startswith('-'):
        option = sys.argv[1][1:]
        if option.lower() == 'help' or option.lower() == 'h':
            print("Options include:\n \
                -version : prints the version number\n \
                -v, -V   : same as -version\n \
                -help    : display this help\n \
                -h , -H  : same as -help \n \
                运行模式 : python primes.py 2 100 ") 
        elif option.lower() == 'version' or option.lower() == 'v':
            print("Version 0.1")
        else:
            print("Unknown option")
            sys.exit()
    
    elif len(sys.argv) < 3:
        print("请输入两个数字, Usage: primes <first number> <second number>")
        sys.exit()
    else:
        start,end = int(sys.argv[1]), int(sys.argv[2])
        #print(start,end,sys.argv[1:])
        #for prime in get_primes(int(start),int(end)):
        #print("介于[%d, %d]的质数序列为 %s" % (start,end,list(get_primes(start,end))))
        print("primes between [%d, %d] = %s" % (start,end,list(get_primes(start,end))))
    """    
    """    #max = 50
    max = input("input max number:")
    max = int(max)
    #print(sum_of_primes.__doc__)
    print("<=%d的所有质数之和为 %d " % (max, sum_of_primes(max)))   
    """