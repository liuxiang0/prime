#!/usr/bin/python
# -*- coding = utf-8 -*-
"""
Print the multiplication table
"""


def multipliction_table(m, n, fn=None):
    for i in range(1,m+1):
        for j in range(1,n+1):
            print("{i}x{j}={n}".format(i=i,j=j,n=i*j), end=',')
        print('\n')

if __name__=='__main__':
    m, n = 19, 19
    multipliction_table(m, n)