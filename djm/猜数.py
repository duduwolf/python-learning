import random

secret = random.randint(1,100)
guess = 0
tries = 0

print("我有一个数，你可以猜一猜。它在1到100之间，你有7次机会")

while guess !=secret and tries < 7:

    guess = int(input('你猜哪个数？'))
    if guess < secret:
        print("你猜小了。")
    elif guess > secret:
        print("你猜大了。")
    tries = tries + 1

if guess == secret:
    print("你猜对了")
else:
    print("你的次数用光了！")
    print("这个数是",secret)
