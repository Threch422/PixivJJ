import user_info as user

# Preset for login
baseUrl = "https://accounts.pixiv.net/login?lang=zh_tw&source=pc&view_type=page&ref=wwwtop_accounts_index"
LoginUrl = "https://accounts.pixiv.net/api/login?lang=zh_tw"

# Fill in this var
cookie = ""

loginHeader = {  
#'origin': "https://accounts.pixiv.net",  
'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",  
'referer': "https://accounts.pixiv.net/login?lang=zh_tw&source=pc&view_type=page&ref=wwwtop_accounts_index",
"cookie": cookie
}  
return_to = "http://www.pixiv.net/"  
pixiv_id = user.account
password = user.password
