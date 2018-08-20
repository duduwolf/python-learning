import random
import easygui

secret = random.randint(1,100)
guess = 0
tries = 0

easygui.msgbox("我有一个数，你可以猜一猜。它在1到100之间，你有7次机会")

while guess !=secret and tries < 7:

    guess = easygui.integerbox('你猜哪个数？')
    if guess < secret:
        easygui.msgbox("你猜小了。")
    elif guess > secret:
        easygui.msgbox("你猜大了。")
    tries = tries + 1

if guess == secret:
    easygui.msgbox("你猜对了")
else:
    easygui.msgbox("你的次数用光了！")
    easygui.msgbox("这个数是",secret)
