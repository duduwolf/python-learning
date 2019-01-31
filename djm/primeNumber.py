def comput(num):
    print("您输入的数字为：%s，现在开始求它的质数===>" %(num))
    isPrime = True
    pList = []
    for i in range(2, num):
        isPrime = True
        for j in range(2, i):
            if (i % j == 0):
                isPrime = False

        if (isPrime):
            pList.append(i)
        
        isPrime = True

    print(pList)





comput(20)