from urllib.parse import parse_qs
from instabot import Bot
import os 
from time import sleep

path = "C:/src/insta_s/content/"

for i in range(3):
    try:
        content = os.listdir(path)
        list0 = ("shop","store","book","present","shpo","stoer")
        print(content[0])
        if  "a" in content[0]:
            os.remove(path+content[0])
    except:
        pass

