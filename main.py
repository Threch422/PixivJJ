import requests
import re
import os
import time
import login as l
import downloadImg as d

def start():
    l.login()
    ID = input("Enter illustartor ID to download all the images he/she draws: ")
    d.downloadImg(d.getAuthorImgDict(ID))

start()