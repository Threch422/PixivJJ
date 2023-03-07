import requests
import time
import preset as p
import user_info as user
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

s = requests.session()

# Using undetected_chromedriver to escape from bot detection
def login():
    login_url = "https://pixiv.net"
    driver = uc.Chrome()

    driver.get(url = login_url)
    login_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Login")
    login_btn.click()

    username = driver.find_element(By.CLASS_NAME, "sc-bn9ph6-6.degQSE")
    password = driver.find_element(By.CLASS_NAME, "sc-bn9ph6-6.hfoSmp")

    username.send_keys(user.account)
    password.send_keys(user.password)
    password.submit()

    time.sleep(3)
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


