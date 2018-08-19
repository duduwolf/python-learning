import easygui

yn = easygui.ynbox('请问你是男的吗？')
if yn == True:
    easygui.msgbox('本程序不欢迎男士')