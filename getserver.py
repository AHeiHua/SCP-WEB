import json
import requests
import re
import getms
url = "http://alobgames.com:8080/getserverlist"
a = requests.get(url)
max_text = a.text
aa = json.loads(max_text)
max = aa['max']
def getlist():
    serverlist = []
    for page in range(1,max+1):
        headers = {
        "User-Agent": "UnityPlayer/2023.2.0b1 (UnityWebRequest/1.0, libcurl/8.1.1-DEV)",
        "Accept": "*/*",
        "Accept-Encoding": "deflate, gzip",
        "page": str(page),
        "platform": "Android",
        "ver": "26",
        "data_ver": "1",
        "X-Unity-Version": "2023.2.0b1"
        }
        res = requests.get(url,headers=headers)
        text = res.text
        text_msg = json.loads(text)
        for i in range(9):
            a = text_msg.get(str(i))
            if a != None:
               name = a.get("name")
            aaaa = text_msg.get(str(i))
            if aaaa != None:
               ip = aaaa.get('ip')
               tag = aaaa.get("tags")
            if tag == ";notmodded":
               iftags = "是"
            else:
               iftags = "否"
            aaaaa = text_msg.get(str(i))
            if aaaaa != None:
                player = aaaaa.get("players").split("/")
            name1 = re.sub(r"<color=(\w+)>(.*?)</color>", r'<i style="color:1;">\2<i>', name)
            serverlist.append(f"{name1}\n是否纯净服:{iftags}\n最大人数:{player[1]}\n当前人数:{player[0]}</br>")

    return serverlist
