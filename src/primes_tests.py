# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:33:11 2018

@author: liu xiang
Test Prime Package

"""
from pyprimes import primes_generator, is_mersenne, digital_number
from pyprimes import primes_sieve1, primes_nth, primes
from pyprimes import rwh_primes3, primes_npsieve3a, primes_npsieve3b, primes_npsieve6
from pyprimes import rwh_primes2
import time
from  os import path as osp


def test_primes_sieve1(n):
    #LIMIT = 10**6
    LIMIT = n
    s = time.time()
    plist = primes_sieve1(LIMIT)
    print("Elapsed(s): {T}.".format(T=time.time() - s))
    print(plist)
    print("Count is {C}, Sum is {S}.".format(C=len(plist), S=sum(plist)))

def test_primes_generator(n):
    if not osp.exists('mesernneprime.txt') :
        outfile = open('mesernneprime.txt','w')
    else:
        outfile = open('mesernneprime.txt','a')
        
    #primes_max = 5000
    primes_max = n
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
                    d = digital_number(mp), p=pm, mp=mp)
                )
            print("MP=2^{p}-1={m} is Mersenne Prime!\n".format(
                    p=pm, m=2**pm-1)
                )
    
    outfile.write("Finished, time = %s \n" % time.strftime("%Y-%m-%d %H:%M:%S"))
    outfile.write("Finished, elasped(s): %d. \n " % (time.time()-start))
    
    outfile.close()


def test_mersenne_prime(n):
    pass


def test_primes_nth(n):
    """
    Testing primes_nth(10000)=104729, Elasped time(s):0.2312018871307373
    Testing primes_nth(100000)=1299709, Elasped time(s):7.670881032943726
    Testing primes_nth(1000000)=15485863, Elasped time(s):248.56228494644165
    """
    # Begin Testing primes_nth(n)
    start = time.time()
    pn    = primes_nth(n)
    end   = time.time()
    print("Testing primes_nth({n})={p}, Elasped time(s):{T}".format(
            n=n, p=pn, T=end-start)
        )
    # End testing primes_nth(n)

def test_primes(n):
    # Begin testing primes(n, filename=None)
    max_p = n
    output_file = 'primes_list' + str(max_p) + '.txt'
    start = time.time()
    primes(max_p, filename=output_file)
    end   = time.time()
    print("Testing primes({n}, filename={f}), elasped time(s):{T}".format(
            n=max_p, f=output_file, T=end-start)
        )
    # end testing primes(n, filename=None)

# test data        
if __name__ == '__main__':
    n = 10**5
    test_primes_sieve1(n)
    
    test_primes_nth(n)
    test_primes(n)
    
    test_primes_generator(n)


    n = 10**8

    start = time.time()
    result = rwh_primes3(n)
    end = time.time()
    print("rwh_primes3({n}), Time(s):{T}".format(n=n, T=end-start))
    print("Primes count: {c} and sum: {s}".format(c=len(result), s=sum(result)))
    
    start = time.time()
    result = primes_npsieve3a(n)
    end = time.time()
    print("primes_npsieve3a({n}), Time(s):{T}".format(n=n, T=end-start))
    print("Primes count: {c} and sum: {s}".format(c=len(result), s=sum(result)))
    
    start = time.time()
    result = primes_npsieve3b(n)
    end = time.time()
    print("primes_npsieve3b({n}), Time(s):{T}".format(n=n, T=end-start))
    print("Primes count: {c} and sum: {s}".format(c=len(result), s=sum(result)))
    
    start = time.time()
    result = primes_npsieve6(n)
    end = time.time()
    print("primes_npsieve6({n}), Time(s):{T}".format(n=n, T=end-start))
    print("Primes count: {c} and sum: {s}".format(c=len(result), s=sum(result)))

    start = time.time()
    result = rwh_primes2(n)
    end = time.time()
    print("rwh_primes2({n}), Time(s):{T}".format(n=n, T=end-start))
    print("Primes count: {c} and sum: {s}".format(c=len(result),s=sum(result)))


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