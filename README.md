# PixivJJ

Download illustrations from the great blue website -- Pixiv

### Current Version: 5/2021

#### Update History:
Ver 1.0: 5/9/2020

Ver 2.0: 15/2/2021

1. Support downloading images from specified illustrator. Auto create folder if folder for illustrator is not existing.
2. Support downloading images from pixiv monthly rank.

Ver 3.0: 17/5/2021

#### Required library and tools:

1. BeautifulSoup4
2. selenium
3. webdriver

You can simply use the `pip install BeautifulSoup4` and `pip insall selenium` to finish the installation of the libraries.

Moreover, please go to https://chromedriver.chromium.org/ to download the Chrome webdriver and put it into the directory which is in your PATH variable of your computer (Suggested putting in the Python directory).

#### How to use?
There are 2 different version, one is the multiple python files version and another is single .exe version. For single .exe version, you are not required to install the python library in your computer. However, webdriver is still needed. Python version allows you to change the default path and other setting in the tool but .exe version is not allowed.



<u>For Python files version</u>:

1. Open **user_info.py**, fill in the path you want to keep your downloaded images. Example: `D:\Hello\PixivCollection\`.
2. Run the **main.py**. If webdriver is put in the correct directory, you should see a Chrome browser pops out.
3. Login your Pixiv account in that Chrome window, default the login time is set as 15 second as it is very sufficient for the developer to login. If you are not, go to **login.py** and change the time of the code `time.sleep(15)` to larger value.
4. After logged in Pixiv, just wait a moment and the Chrome window will close automatically. It is just used to grab the cookie.
5. Follow the instruction in the command prompt, 0 represents downloading images from specific Pixiv user and you need to enter his/her Pixiv ID later. 1 represents downloading the current monthly rank of Pixiv.

Remark: Default the number of images are restricted to 50. You can change it in the code also which is in **downloadImg.py** line 51 `for i in range(50)`.



<u>For .exe version</u>

It is the single file version using `pyinstaller` for the packing.

1. Under the same directory of **main.exe**, create a file named as **Pixiv**.
2. Then just follow the same instruction from the Python version step 3.



##### Example of Pixiv illustrator ID:

Here is the main page link of illustrator Anmi in Pixiv:

https://www.pixiv.net/users/212801

Here, 212801 is the ID of Anmi. So you just enter that ID in the tool.

##### Disclaimer: This tool may contains bugs due to the update in Pixiv website and user should anticipate all bugs of this tool before using it. Please contact developer if bugs occur.