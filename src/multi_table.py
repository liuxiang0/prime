#!/usr/bin/python
# -*- coding = utf-8 -*-
"""
Print the multiplication table
"""


def multipliction_table(m, n, fn=None):
    if fn is None:
        for i in range(1,m+1):
            for j in range(i,n+1):  # right upper triangle, range(1,n+1)
                print("{i}x{j}={n}".format(i=i,j=j,n=i*j), end=' ')
            print('\n')
    else:
        with open(fn,'w') as f:
            for i in range(1, m+1):
                for j in range(1, i+1):  # left lower triangle
                    f.write("{i}x{j}={n} ".format(i=i,j=j,n=i*j))
                f.write('\n')


if __name__=='__main__':
    m, n = 19, 19
    multipliction_table(m, n)
    fn = r'multi.md'
    multipliction_table(m, n, fn)
