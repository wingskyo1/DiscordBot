from riotwatcher import LolWatcher, ApiError
import time
import winsound

# golbal variables
api_key = 'RGAPI-3cff2400-bb92-42d5-8d1d-0f762f4f5441'
watcher = LolWatcher(api_key)
my_region = 'kr'
userName = input('請輸入妳要追蹤的使用者名稱：')
# userName = 'ziyunS2'
gameStatus = False
waitSecond= 60
print("Script 執行開始! 偵測中~ \n偵測對象 : " + userName + "\n每" + str(waitSecond) +"秒偵測一次\n")

while True:

    player = watcher.summoner.by_name(my_region, userName)

    try:
        spector = watcher.spectator.by_summoner(my_region, player['id'])
        gameStatus = True

    except:
        print("還沒開始遊戲")
        gameStatus = False

    if gameStatus == True:
        winsound.MessageBeep(0)

    time.sleep(waitSecond)
