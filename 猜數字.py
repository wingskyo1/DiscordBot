import random
import functiona as 函式庫


pw = 函式庫.GetRandomFourNumber()
函式庫.WelcomeMessage(pw)
guess = input('請猜一組四位數：')
print("===========================")

while pw != guess:

    while guess.isdigit() == False or len(guess) != 4:
        guess = input('我要的是一組「四位數」！看不懂中文嗎！？\n請猜一組四位數：')
        print("===========================")

    c = sum(a==b for a, b in zip(guess, str("".join(pw))))
    print(c)
    a = int(0)
    b = int(0)
    if int(guess[0]) == pw[0]:
        a = a + 1
    if int(guess[1]) == pw[1]:
        a = a + 1
    if int(guess[2]) == pw[2]:
        a = a + 1
    if int(guess[3]) == pw[3]:
        a = a + 1
    else:
        a = a + 0

    if int(guess[0]) == pw[1] or int(guess[0]) == pw[2] or int(guess[0]) == pw[3]:
        b = b + 1
    if int(guess[1]) == pw[0] or int(guess[1]) == pw[2] or int(guess[1]) == pw[3]:
        b = b + 1
    if int(guess[2]) == pw[0] or int(guess[2]) == pw[1] or int(guess[2]) == pw[3]:
        b = b + 1
    if int(guess[3]) == pw[0] or int(guess[3]) == pw[1] or int(guess[3]) == pw[2]:
        b = b + 1
    else:
        b = b + 0

    print(a, "A", b, "B")
    print("有", a, "個數字正確，且位置正確")
    print("有", b, "個數字正確，但位置錯誤")
    print("===========================")
    if int(a) == 4:
        break
    guess = input('請猜一組四位數：')
    print("===========================")

if int(a) == 4:
    print("恭喜你答對了！！！！！\n答案是：", pw)
    print()