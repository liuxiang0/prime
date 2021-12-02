r"""求日期组成的八位数(形如 yyyymmdd)是否为素数？
问题来源：吴宗敏
日期：2021-10-1 国庆72周年
coded by: [刘翔](https://geogebra.com/m/kumath) &copy; <kumath@outlook.com>
20210929，20211001，10012021,9292021 都是素数(吴宗敏)
"""

from sympy import primerange
from sys import argv
from datetime import datetime


def isleapyear(year):
    '''Python program to check if year is a leap year or not'''

    # To get year (integer input) from the user
    # year = int(input("Enter a year: "))

    return (year % 4) == 0 and (year % 100 !=0) or (year % 400) == 0

# 一条Python语句判断是否为闰年？
isleap = lambda year: (year % 4) == 0 and (year % 100 != 0) or (year % 400) == 0

def date_isprime(year1, year2):
    '''给定两个年份，得到 yyyymmdd 是素数的列表
    input: 起止年份 year1, year2
    output：素数列表(按照年份分类)
    '''

    bmonths = [31,28,31,30,31,30,31,31,30,31,30,31]  # 月份对应的常规天数，闰年除外
    
    res = []
    for year in range(year1, year2):
        r1 = []
        leap = isleap(year)   # isleapyear(year)
        bmonths[1] = 29 if leap else 28
        
        for month in range(1, 13):
            ymd = [str(year), str(month).zfill(2), '1'.zfill(2)]
            lower = ''.join(ymd) 
            ymd = [str(year), str(month).zfill(2), str(bmonths[month-1]+1)]
            upper = ''.join(ymd)
            primes = primerange(int(lower) , int(upper))
            # r1.append()         ## append是在末尾追加的意思
            r1 += list(primes)    ## 合并merge两个列表lists

        res.append(r1)            ## 按照年份在末尾追加到列表

    return res



if __name__ == '__main__':
    if len(argv) > 1 and argv[1].lower() in ['--help', '-h', '-help']:
        print("""
        给定两个年份之间，日期是素数的列表。
        使用说明：python prime_date.py 起始年份 [终止年份, 缺省是当前年份]
        使用举例：python prime_date.py 2000 2011
                  python prime_date.py 2010
                  python prime_date.py %[显示当前年份的素数日期]
                  python prime_date.py --help
                  python prime_date.py -h
        """)
        exit()

    year = datetime.now().year
    sy = argv[1] if len(argv) > 1 else str(year)
    if isinstance(sy,(str)):
        starty = int(sy)
    else:
        raise ValueError

    ey = argv[2] if len(argv) > 2 else str(year+1)
    if isinstance(ey,(str)):
        endy = int(ey)
    else:
        raise ValueError

    print('起止年份 {0}年~{1}年，素数日期有\n'.format(starty, endy))
    for yp in date_isprime(starty, endy):
        print('{0}, 个数 {1}\n'.format(yp, len(yp)))
