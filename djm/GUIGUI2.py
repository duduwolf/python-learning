import easygui
import random

qq = easygui.msgbox("我们来玩石头剪刀布吧！")
print(qq)
yn = True

while qq == "OK" and yn == True:
    a = easygui.buttonbox("你出什么？",choices=["石头","剪刀","布"])
    d = random.randint(1,3)
    if a == "石头":
        a = 3
    if a == "剪刀":
        a = 2
    if a == "布":
        a = 1

    if a - d == 1 or a - d == -2:
        yn = easygui.ynbox("恭喜恭喜，你赢了！再来一把？")

    if a - d == 2 or a - d == -1:
        yn = easygui.ynbox("很遗憾，你输了。再来一把？")
    if a - d == 0:
        ww = easygui.msgbox("平手")
        yn = True