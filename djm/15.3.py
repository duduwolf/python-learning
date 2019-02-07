import time
import AA

v = True

while v == True:
    a = input("请输入第一个要计算的数字：")
    if a == "out" :
        break
    b = str(input("请输入计算符号："))
    if a == "out" or b == "out" :
        break
    c = input("请输入第二个要计算的数字：")
    if a == "out" or b == "out" or c == "out" :
        break
    if a != "out":
        a = int(a)
    if c != "out":
        c = int(c)
    d = str(AA.计算(a,b,c))
    print("得数是: " + d)
    time.sleep(2)