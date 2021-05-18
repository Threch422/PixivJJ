import requests
import time
import preset as p
from selenium import webdriver

s = requests.session()

# depreicated
''' 
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
        return "Unauthorized Access. Please check your cookie and login status in Pixiv"
    else:
        return "Login successfully"
'''
# Using selenium and webdriver
def login():
    login_url = "https://pixiv.net"
    driver = webdriver.Chrome()
    driver.get(url = login_url)
    time.sleep(15)  # time for login
    driver.refresh()
    cookies = driver.get_cookies()
    cookie_str = ""
    # Grab the cookies and reassemble it
    for cookie in cookies:
        item_str = cookie["name"] + "=" + cookie["value"] + ";"
        cookie_str += item_str
    p.cookie = cookie_str
    driver.quit()
    time.sleep(1)


