#coding=utf-8
'''
我们
'''

def main():

    '''
    #练习1
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if(i!=j) and (j!=k) and (i!=k):
                    print i,j,k
    '''

    '''
    #练习2
    i = int(raw_input('净利润:'))
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for idx in range(0,6):
        if i>arr[idx]:
            r+=(i-arr[idx])*rat[idx]
            print(i-arr[idx])*rat[idx]
            i = arr[idx]
    print r
    '''
    
    '''
    #练习3
    for i in range(1,85):
        if 168%i == 0:
            j = 168/i
            if i>j and (i+j)%2==0 and (i-j)%2==0:
                m = (i+j)/2
                n = (i-j)/2
                x = n*n - 100
                print x
    '''

    '''
    #练习4
    year = int(raw_input('year:\n'))
    month = int(raw_input('month:\n'))
    day = int(raw_input('day:\n'))

    months = (0,31,59,90,120,151,181,212,243,273,304,334)
    if 0 < month <=12:
        sum = months[month-1]
    else:
        print 'data error'
    sum += day
    leap=0
    if(year%400 == 0) or ((year%4 == 0) and (year%100 !=0)):
        leap = 1
    if(leap==1) and (month>2):
        sum+=1
    print 'it is the %dth day.' %sum
    '''
    '''
    #练习5
    l = []
    for i in range(3):
        x = int(raw_input('integer:\n'))
        l.append(x)
    l.sort()
    print l
    '''
    
    '''
    #练习6
    def fib(n):
        if n==1 or n==2:
            return 1;
        return fib(n-1)+fib(n-2)
    print fib(10)
    '''

    #练习7
    a = [1,2,3]
    b= a[:]
    print b

    #练习8
    for i in range(1,10):
        print
        for j in range(1, i+1):
            print("%d*%d=%d" %(i, j, i*j)),
    
    #练习9
    #题目：暂停一秒输出。
    #程序分析：使用 time 模块的 sleep() 函数。

    import time
    myD = {1:'a', 2:'b'}
    for key, value in dict.items(myD):
        print key, value
        time.sleep(2)
    
    import time
    print time.strftime('%Y-%m-%d')


main()
