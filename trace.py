import requests
from lxml import etree
import time
import os
#from sendemail import email

while True:
    #url = "https://www.op.gg/summoner/spectator/userName=ziyunS2&"  
    #url = "https://www.op.gg/summoner/spectator/userName=ziyunS2&"   
    url = "https://www.op.gg/summoner/userName=ziyunS2&" 
    test = requests.get(url)
    content = requests.get(url).content 
    html = etree.HTML(content)
    title = html.xpath("/html/body")[0]


    if not os.path.isfile("E:\\title_temp.txt"):

        f = open("E:\\title_temp.txt", "w")
        f.write(title)

        f.close()
    else:

        with open("E:\\title_temp.txt", "r+") as f:
            old_title = f.read()
            if old_title !=title:

                f.seek(0)
                f.truncate()                             

                f.write(title)

                break
            
            else:
           
                print("321\n")
    time.sleep(5)
