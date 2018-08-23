import easygui
import random

qq = easygui.msgbox("我们来玩一个游戏")
yn = True

while qq == "OK" and yn == True:
    a = int(easygui.buttonbox("你出多少",choices=["0","5","10"]))
    if a == 0:
        b = int(easygui.buttonbox("你预判多少",choices=["0","5","10"]))
    if a == 5:
        b = (easygui.buttonbox("你预判多少",choices=["5","10","15"]))
    if a == 10:
        b = int (easygui.buttonbox("你预判多少",choices=["10","15","20"]))
    c = random.randint(1,3)
    d = random.randint(1,5)
    while c > d and d - c > 2:
        d = random.randint(1,5)

    if c == 1:
        c = 0
    if c == 2:
        c = 5
    if c == 3:
        c = 10
    if d == 1:
        d = 0
    if d == 2:
        d = 5
    if d == 3:
        d = 10
    if d == 4:
        d = 15
    if d == 5:
        d = 20

    if a + c == b and a + c != d:
        yn = easygui.ynbox("恭喜恭喜，你赢了！再来一把？")
    if b == d or (a + c != b and a + c != d):
        easygui.msgbox("平手，再来！")
    else:
         yn = easygui.ynbox("很遗憾，你输了。再来一把？")