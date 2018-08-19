#-*- coding:utf-8 -*-
#花式打印
#Author Name: Ailsa
symbol=input('Please input your symbol:')
outnum=int(input('Please input the line number you want:'))
for i in range(1,outnum):
    j = outnum - i
#打印出首部的空格
    print(' ' * j, symbol, end='')
#循环打印后面的空格和字符
    for i2 in range(i-1):
        print(' '* outnum,symbol,end='')
    print('')
#打印下半部分
for i in range(outnum):
    j = outnum-i
    print(' ' * i, symbol, end='')
    for i2 in range(j-1):
        print(' '* outnum,symbol,end='')
    print('')
