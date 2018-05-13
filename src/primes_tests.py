# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:33:11 2018

@author: abc
Test Prime Class

"""
from primes import Prime

import time
from  os import path as osp

# test data        
if __name__ == '__main__' :
    
    if not osp.exists('mesernneprime.txt') :
        outfile = open('mesernneprime.txt','w')
    else:
        outfile = open('mesernneprime.txt','a')
        
    p = Prime(4000)   # if n =4000, elasped time = 49secondes in my notebook ThinkPad E450
    primes = p.PrimesList()  # get prime list between [2,4000]
    primelist = list(primes) # change iteration to list
    # print the above prime list 
    print( primelist)
    # start time for running
    start_time = time.time()
    outfile.write("Testing, time = %s \n" % time.strftime("%Y-%m-%d %H:%M:%S"))
   
    for i in primelist:  # every i is prime
        if p.MPLLtest(i):  # Mesernne Prime Testing by Lucas_Lehmer_Test
            mp = 2**i -1
            tmp = Prime(mp)
            outfile.write("DC=%d, MP(%d) = 2**%d-1 = %d \n" % (tmp.NumberofDigital(),i,i,mp))
            print("MP=2**%d-1=%d is Mersenne Prime!\n" % (i,2**i-1))
   
    
    outfile.write("Finished, time = %s \n" % time.strftime("%Y-%m-%d %H:%M:%S"))
    outfile.write("Finished, elasped time: %d seconds. \n " % (time.time()-start_time))
    
    outfile.close()
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