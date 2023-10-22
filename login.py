import requests
import json

def login(name,password):
    userdata = {}
    url = "http://alobgames.com:8080/login"
    headers = {
    "User-Agent": 'UnityPlayer/2023.2.0b1 (UnityWebRequest/1.0, libcurl/8.1.1-DEV)',
    'Accept': '*/*',
    'Accept-Encoding': 'deflate, gzip',
    'login': name,
    'password':password,
    'platform': 'Android',
    'ver': '26',
    'data_ver': '1',
    'X-Unity-Version': '2023.2.0b1'
    }
    res = requests.get(url,headers=headers)
    text = res.text
    data = json.loads(text)
    """ 获取登录密钥 """
    if "secret" in text:
        secret = data["secret"]
        id = data['id']
        login_msg = "已登录"
    else:
        login_msg = "登录失败"

    if login_msg != "登录失败":
        userdata = {
            "msg": login_msg,
            "secret": secret,
            "id": id
        }
    else:
        userdata = {
            "msg": login_msg,
        }
    json_str = json.dumps(userdata)
    return json_str