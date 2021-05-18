
# Preset for login
baseUrl = "https://accounts.pixiv.net/login?lang=zh_tw&source=pc&view_type=page&ref=wwwtop_accounts_index"
LoginUrl = "https://accounts.pixiv.net/api/login?lang=zh_tw"

# Fill in this var
cookie = ""

loginHeader = {  
#'origin': "https://accounts.pixiv.net",  
'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",  
'referer': "https://accounts.pixiv.net/login?lang=zh_tw&source=pc&view_type=page&ref=wwwtop_accounts_index",
#"cookie": cookie
}

rankingHeader = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36",
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    "cookie" : cookie,
    'referer': 'https://www.pixiv.net'   
}

return_to = "http://www.pixiv.net/"  

