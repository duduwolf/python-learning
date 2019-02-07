def 计算 (a,x,b):
    rst = 0
    if x == "+":
        rst = a+b
    if x == "-":
        rst = a-b
    if x == "*":
        rst = a*b
    if x == "/":
        rst = int(a/b)
    return rst


def 长方形面积 (a,b):
    print (str(a*b))


def 三角形面积 (a,b):
    print (str(a*b/2))


def 梯形面积 (a,b,c):
    print (str((a+b)*c/2))


def 圆形面积 (a):
    print (str((a*a)*3.1415926535787))