# 否定：False  确定：true
import easygui
d =  easygui.ynbox('你今天过的好吗？')
if d == True:
    jm = easygui.ynbox('那太好了！和你聊天我很高兴，你觉得呢？')
    if jm == True:
        easygui. msgbox('那我们就聊到这吧。')
    if jm == False:
        easygui.msgbox('好吧,那我就另找其人吧。')
else:
    djm = easygui.ynbox('我认为明天会更好的。 你觉得呢？')
    if djm == True:
        easygui.msgbox('我们的观点一致，你真是我的知音。')
    if djm == False:
        easygui.msgbox('乐观一点嘛。')