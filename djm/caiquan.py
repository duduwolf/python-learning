# 高级版猜拳
# 学习条件判断、循环、easygui
import random
import easygui

quandict = {'石头':3, '剪子':2, '布':1}
go_on = True
computer = random.randint(1,3)
is_tie = False

while go_on == True:
    # 每次循环，电脑都重新出拳
    computer = random.randint(1,3)
    if is_tie == False:
        msg = '请使出你的洪荒之力，看看能不能猜赢电脑:)'
    else:
        msg = '这把是平局，请继续猜...'

    result = int(quandict[easygui.buttonbox(msg, '你 VS 电脑', choices=['石头', '剪子', '布'])]) - computer
    is_tie= False

    if result == 0:
        is_tie = True
        continue
    elif result == 1 or result == -2:
        go_on = easygui.ynbox('恭喜你赢了,是否继续和电脑猜一局？')
    else:
        go_on = easygui.ynbox('很遗憾你输了，是否继续和电脑猜一局？')