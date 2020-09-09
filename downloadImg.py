import requests
import re
import os
import time
import login as l
import preset as p
import user_info as user

def getAuthorImgDict(author_ID):
    author_Img_Dict_header = {
    "referer": "https://www.pixiv.net/ajax/user/" + author_ID + "/profile/all?lang=zh_tw",
    "cookie" : p.cookie
    }
    request = l.s.get("https://www.pixiv.net/ajax/user/" + author_ID + "/profile/all?lang=zh_tw", headers = author_Img_Dict_header)
    global false, null, true
    false = 'False'
    null = 'None'
    true = 'True'
    author_img_dict = eval(request.text)['body']
    author_img_dict = list(author_img_dict.get('illusts', {}).keys())
    return author_img_dict

def downloadImg(author_img_dict, author_ID):
    img_dict = []
    # Creating new directory
    author_page = l.s.get('https://www.pixiv.net/users/{}'.format(author_ID), headers = {
        'referer': 'https://www.pixiv.net/users/{}'.format(author_ID)
    }).text
    author_name = re.findall('<title>(.*?) - pixiv</title>',author_page)[0]
    if not(os.path.isdir(user.path + author_name)):
        os.mkdir(user.path + author_name)
    new_path = user.path + '/' + author_name + '/'

    for i in range(len(author_img_dict)):
        target = "https://www.pixiv.net/artworks/" + author_img_dict[i]
        target = l.s.get(target).text
        img_url = re.findall('{"mini":".*?","thumb":".*?","small":".*?","regular":".*?","original":"(.*?)"}', target)
        img_url = img_url[0]
        img_dict.append(img_url)

    for j in range(len(img_dict)):
        header = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36",
        'Referer': "https://www.pixiv.net/artworks/" + author_img_dict[j]
        }
        img_response = l.s.get(img_dict[j], headers = header)
        img = img_response.content
        file_name = new_path + '{}'.format(author_img_dict[j]) + '.jpg'
        # Check file existing or not, if yes, skip downloading process
        if os.path.isfile(file_name):
            continue
        with open(file_name, 'wb') as jpg:
            jpg.write(img)
            print("Downloaded: " + str(j+1) + " / " + str(len(img_dict)))
        if (j % 40 == 0):
            time.sleep(2)
    print("End")
