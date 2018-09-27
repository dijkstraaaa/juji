import requests
import json
import string
from bs4 import BeautifulSoup

login = "http://code.t-appagile.com/users/sign_in"
call = "http://code.t-appagile.com/users/auth/ldapmain/callback"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cache-Control': 'no-cache',
    # 'Content-Length':'183',

    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '',
    'Host': 'code.t-appagile.com',
    'Origin': 'http://code.t-appagile.com',
    'Proxy-Connection': 'keep-alive',

    'Referer': 'http://code.t-appagile.com/users/sign_in',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}


def HttpPost(apiUrl, data):
    try:
        global headers
        r = requests.post(apiUrl, headers=headers, data=data)

        cook = r.request.headers["Cookie"].split('=')
        lowCook = headers["Cookie"].split('=')

        newCook = lowCook[0] + '=' + lowCook[1] + '=' + cook[2]
        headers["Cookie"] = newCook
        print("登陆成功：", newCook)
        return r
    except:
        return


def HttpGet(apiUrl):
    try:
        global headers
        r = requests.get(apiUrl)
        cook = ""
        for c in r.cookies:
            cook += c.name + "=" + c.value + ";"

        headers["Cookie"] = cook
        print("登陆前的：", cook)

        return r.text
    except:
        return


def HttpGetLcmm(apiUrl):
    try:
        r = requests.get(apiUrl, headers=headers)
        return r.text
    except:
        return


res = HttpGet(login)
html = BeautifulSoup(res, "html.parser")

token = html.find_all(type="hidden")[1]["value"]

postData = {}
postData["utf8"] = "✓"
postData["authenticity_token"] = token
postData["username"] = "你的账号"
postData["password"] = "你的密码"

res = HttpPost(call, postData)

# print(res.status_code)
# print(res.text)
# print(html)

res = HttpGetLcmm("http://code.t-appagile.com/SI.Web/lcmm-web")
print('ok!')