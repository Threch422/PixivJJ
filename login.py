import requests
import re
import os
import time
import user_info as user
import preset as p

s = requests.session()

def login():
    # Getting post_key
    post_key_html = s.get(p.baseUrl, headers = p.loginHeader).text
    reg = r'name="post_key" value="(.*?)"'
    re_key = re.compile(reg)
    post_key = re.findall(re_key, post_key_html)
    data = {
        'pixiv_id': p.pixiv_id,
        'password': p.password,
        'return_to': p.return_to,
        'post_key': post_key
    }
    rep = s.post(p.LoginUrl, data = data, headers = p.loginHeader)
    if (rep.status_code == 401):
        print("Unauthorized Access. Please check your cookie and login status in Pixiv")
    else:
        print("Login successfully")
