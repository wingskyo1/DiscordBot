import random

def GetRandomFourNumber():
    pw_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    randomFourNumber = []
    for i in range(4):
        R = (random.choice(pw_list))
        pw_list.remove(R)
        randomFourNumber.append(R)
    return randomFourNumber

def WelcomeMessage(pw):
    print("為了你方便檢查，\n先偷偷告訴你答案是：", pw)
    print()
    print("===========================")
