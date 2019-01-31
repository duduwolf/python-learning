a = int(input("输入动物总数:"))
b = int(input("输入脚的总数:"))
x = int(input("输入1个A动物的所有脚:"))
y = int(input("输入1个b动物的所有脚:"))

if x > y:
    t = int((a*x-b)/(x-y))
    j = int(a-t)
    print("A动物有"+str(t)+"只")
    print("B动物有"+str(j)+"只")

if x < y:
    T = int((a*y-b)/(y-x))
    J = int(a-T)
    print(str(x)+"只脚的动物有"+str(T)+"只")
    print(str(y)+"只脚的动物有"+str(J)+"只")

if x == y:
    print("无法计算")