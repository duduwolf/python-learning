a = int(input("请输入一个数字："))
b = 0
c = True
while c == True :
    b = b+1
    d = 3*b
    if d <= a:
        print (str(d))
        c = True
    if d > a:
        c = False