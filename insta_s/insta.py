from instabot import Bot
import os 
from time import sleep

print("bot has been started.")

path = "../content/"
un = ""
pw = ""

sleep =21000
#seconds after per post

#login and upload
bot = Bot()

bot.login(username=un,password=pw)

hastags = "# #instagood #instagram #photography  #happy #together #photooftheday #explore"
#list content
content = os.listdir(path)

print(content)


while True:
    try:
        
        a = content[0]
        #decide content type
        if ".jpg" in a:
            bot.upload_photo(a, caption=hastags)
        else:
            pass

        if ".mp4" in a:
            bot.upload_video(a, caption=hastags)
        else:
            pass


        #used content removed
        os.remove(path+a)

        print("content uploaded.", len(content),"content left." )
        sleep(sleep)

    except Exception as e:
        print(e)
