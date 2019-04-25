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

np_sieve_primes3a(100000000), Time(s):3.614898920059204
Primes count: 5761455 and sum: 279209790387276
np_sieve_primes3b(100000000), Time(s):3.4135758876800537
Primes count: 5761455 and sum: 279209790387276
np_sieve_primes6(100000000), Time(s):2.111391067504883
Primes count: 5761455 and sum: 279209790387276
"""