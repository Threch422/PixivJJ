import requests
import re
import os
import time
import login as l
import preset as p
import user_info as user
from bs4 import BeautifulSoup


def getAuthorImgDict(author_ID):
    author_Img_Dict_header = {
    "referer": "https://www.pixiv.net/ajax/user/{}/profile/all?lang=zh_tw".format(author_ID),
    "cookie" : p.cookie,
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"
    }
    request = requests.get("https://www.pixiv.net/ajax/user/{}/profile/all?lang=zh_tw".format(author_ID), headers = author_Img_Dict_header)
    global false, null, true
    false = 'False'
    null = 'None'
    true = 'True'
    author_img_dict = eval(request.text)
    author_img_dict = author_img_dict['body']
    author_img_dict = list(author_img_dict.get('illusts', {}).keys())
    return author_img_dict

# mode: 0 = from specified illustrator, 1 = monthly ranking
def downloadImg(author_img_dict, author_ID, mode):
    img_dict = []
    # Creating new directory
    if (mode == 0):
        author_page = requests.get('https://www.pixiv.net/users/{}'.format(author_ID), headers = {
            'referer': 'https://www.pixiv.net/users/{}'.format(author_ID),
            "cookie" : p.cookie,
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"
        }).text
        author_name = re.findall('<title>(.*?) - pixiv</title>',author_page)[0]
        if not(os.path.isdir(user.path + author_name)):
            os.mkdir(user.path + author_name)
        new_path = user.path + '/' + author_name + '/'
    elif (mode == 1):
        # main page url
        monthly_ranking_url = "https://www.pixiv.net/ranking.php?mode=monthly&content=illust"
        # request page
        rank_data = requests.get(monthly_ranking_url, headers = p.rankingHeader)        
        title_tag = BeautifulSoup(rank_data.text, "lxml").title.string.split(" ", 1)[1]
        if not(os.path.isdir(user.path + title_tag)):
            os.mkdir(user.path + title_tag)
        new_path = user.path + '/' + title_tag + '/'

    for i in range(50):
        if (i >= len(author_img_dict)):
            break
        target_header = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36",
            'Referer': "https://www.pixiv.net/artworks/" + author_img_dict[i],
            'cookie': p.cookie
        }
        target = "https://www.pixiv.net/artworks/" + author_img_dict[i]
        target = requests.get(target, headers = target_header).text
        img_url = re.findall('{"mini":".*?","thumb":".*?","small":".*?","regular":".*?","original":"(.*?)"}', target)
        img_dict.append(img_url[0])

    for j in range(len(img_dict)):
        header = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36",
            'Referer': "https://www.pixiv.net/artworks/" + author_img_dict[j],
            'cookie': p.cookie
        }
        file_name = new_path + '{}'.format(author_img_dict[j]) + '.jpg'
        # Check file existing or not, if yes, skip downloading process
        if os.path.isfile(file_name):
            continue
        # Download
        img_response = requests.get(img_dict[j], headers = header)
        img = img_response.content
        with open(file_name, 'wb') as jpg:
            jpg.write(img)
            print("Downloaded: " + str(j+1) + " / " + str(len(img_dict)))
        if (j % 40 == 0):
            time.sleep(2)
    print("End")

def monthRankingImgDict():
    # main page url
    monthly_ranking_url = "https://www.pixiv.net/ranking.php?mode=monthly&content=illust"
    # request page
    rank_data = requests.get(monthly_ranking_url, headers = p.rankingHeader)

    # parse it
    soup = BeautifulSoup(rank_data.text, "lxml").body.find('div', attrs = {'class': 'ranking-items-container'})
    img_dict = []
    for section in soup.find_all('section', attrs = {'class': 'ranking-item'}):
        artworkID = section.get('data-id')
        img_dict.append(artworkID)
        #print(artworkID)
    return img_dict
            
