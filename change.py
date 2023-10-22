import requests
import json
from urllib.parse import quote

url_jianjie = "http://alobgames.com:8080/changedescription"
url_name = "http://alobgames.com:8080/changenickname"


""" 更改简介和名字的UA """
def getname_ua(id,secret,name):
    name1 = quote(name)
    headers = {
    "User-Agent": 'UnityPlayer/2023.2.0b1 (UnityWebRequest/1.0, libcurl/8.1.1-DEV)',
    'Accept': '*/*',
    'Accept-Encoding': 'deflate, gzip',
    'id': str(id),
    "secret":secret,
    'newnickname': name1,
    'platform': 'Android',
    'ver': '26',
    'data_ver': '1',
    'X-Unity-Version': '2023.2.0b1'
    }
    return headers
"""更改简介的UA"""
def getdes_ua(id,secret,des):
    des1 = quote(des)
    headers = {
        "User-Agent": 'UnityPlayer/2023.2.0b1 (UnityWebRequest/1.0, libcurl/8.1.1-DEV)',
        'Accept': '*/*',
        'Accept-Encoding': 'deflate, gzip',
        'id': str(id),
        "secret":secret,
        'description': des1,
        'platform': 'Android',
        'ver': '26',
        'data_ver': '1',
        'X-Unity-Version': '2023.2.0b1'
    }
    return headers


def change_data_a(id, secret,des,name):
    data_name = []
    res = requests.get(url_jianjie, headers=getdes_ua(id, secret, des))
    aaa = res.text
    msg1 = json.loads(aaa)
    res2 = requests.get(url_name, headers=getname_ua(id, secret, name))
    aa = res2.text
    msg2 = json.loads(aa)
    if msg1["code"] == "cs_0":
        #0
        data_name.append("简介更改成功")
    else:
        #0
        data_name.append("简介更改失败")
    if msg2["code"] == "cs_0":
        #1
        data_name.append("名字更改成功")
    else:
        #1
        data_name.append("名字更改失败")

    return data_name

