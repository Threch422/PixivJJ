import requests
import re
import os
import time
import login as l
import downloadImg as d

def start():
    l.login()
    print("What are you going to do with this tool?\n")
    mode = int(input("0. Download image by illustrator ID.\n1. Downlod images of monthly ranking.\n"))
    if (mode == 0):
        author_ID = input("Enter illustartor ID to download all the images he/she draws: ")
        d.downloadImg(d.getAuthorImgDict(author_ID), author_ID, 0)
    elif (mode == 1):
        d.downloadImg(d.monthRankingImgDict(), 369, 1)
    else:
        print("You are entering invalid choice, tool will be terminated.")

start()