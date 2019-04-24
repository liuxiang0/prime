#!/usr/bin/python
#-*- coding=utf-8 -*-
"""
If you accept itertools but not numpy, here is an adaptation of 
rwh_primes2 for Python 3 that runs about **twice** as fast on my machine. 
The only substantial change is using a bytearray instead of a list for 
the boolean, and using compress instead of a list comprehension to build 
the final list.

Comparison:
rwh_primes2(1000000), Time(s):0.04717898368835449
Primes count: 78498 and sum: 37550402023
rwh_primes2_python3(1000000), Time:0.028133153915405273
Primes count: 78498 and sum: 37550402023
np_primes3a(1000000), Time(s):0.015568971633911133
Primes count: 78498 and sum: 37550402023

rwh_primes2(1000000), Time(s):0.04691505432128906
Primes count: 78498 and sum: 37550402023
rwh_primes2_python3(1000000), Time(s):0.024444103240966797
Primes count: 78498 and sum: 37550402023
np_sieve_primes3a(1000000), Time(s):0.011823892593383789
Primes count: 78498 and sum: 37550402023
np_sieve_primes6(1000000), Time(s):0.012167930603027344
Primes count: 78498 and sum: 37550402023

rwh_primes2(100000000), Time(s):5.320466995239258
Primes count: 5761455 and sum: 279209790387276
rwh_primes2_python3(100000000), Time:2.6664156913757324
Primes count: 5761455 and sum: 279209790387276

rwh_primes2(100000000), Time(s):6.515302896499634
Primes count: 5761455 and sum: 279209790387276
rwh_primes2_python3(100000000), Time(s):2.687973976135254
Primes count: 5761455 and sum: 279209790387276
np_sieve_primes3a(100000000), Time(s):3.7623178958892822
Primes count: 5761455 and sum: 279209790387276
np_sieve_primes6(100000000), Time(s):2.38877272605896
Primes count: 5761455 and sum: 279209790387276

rwh_primes2(100000000), Time(s):5.198900938034058
Primes count: 5761455 and sum: 279209790387276
rwh_primes2_python3(100000000), Time(s):2.6706080436706543
Primes count: 5761455 and sum: 279209790387276
np_sieve_primes3a(100000000), Time(s):3.70415997505188
Primes count: 5761455 and sum: 279209790387276
np_sieve_primes6(100000000), Time(s):1.1421229839324951
Primes count: 5761455 and sum: 279209790387276
"""


import itertools
import time
import numpy as np

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


def np_sieve_primes3a(upto):
    """It sieves a Boolean array referring to its indices only and 
    elicits prime numbers from the indices of all True values. 
    No module needed.
    """
    mat = np.ones((upto), dtype=bool)  # initial all postion True
    mat[0] = False
    mat[1] = False
    mat[4::2] = False  # let all even (>4) position is False
    upper = int(upto ** 0.5)
    for idx in range(3, upper + 1, 2):
        mat[idx*2::idx] = False  # reject the idx's multiple
    return np.where(mat == True)[0]


def np_sieve_primes6(upto):
    primes=np.arange(3, upto+1, 2)
    isprime=np.ones(int((upto-1)/2), dtype=bool)
    upper = int(upto**0.5)
    for factor in primes[:upper]:
        if isprime[int((factor-2)/2)]: 
            isprime[int((factor*3-2)/2):int((upto-1)/2):factor]=0

    return np.insert(primes[isprime],0,2)


if __name__=='__main__':
    n = 10**8

    start = time.time()
    result = rwh_primes2(n)
    end = time.time()
    print("rwh_primes2({n}), Time(s):{T}".format(n=n, T=end-start))
    print("Primes count: {c} and sum: {s}".format(c=len(result),s=sum(result)))

    start = time.time()
    result = rwh_primes2_python3(n)
    end = time.time()
    print("rwh_primes2_python3({n}), Time(s):{T}".format(n=n, T=end-start))
    print("Primes count: {c} and sum: {s}".format(c=len(result), s=sum(result)))
    
    start = time.time()
    result = np_sieve_primes3a(n)
    end = time.time()
    print("np_sieve_primes3a({n}), Time(s):{T}".format(n=n, T=end-start))
    print("Primes count: {c} and sum: {s}".format(c=len(result), s=sum(result)))
    
    start = time.time()
    result = np_sieve_primes6(n)
    end = time.time()
    print("np_sieve_primes6({n}), Time(s):{T}".format(n=n, T=end-start))
    print("Primes count: {c} and sum: {s}".format(c=len(result), s=sum(result)))
