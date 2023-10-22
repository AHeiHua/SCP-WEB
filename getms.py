import requests
import json

def getping(ip):
    url = f"https://api.kit9.cn/api/ping_speed_test/api.php?host={ip}"
    res =requests.get(url)
    data = json.loads(res.text)
    code = data['code']
    if code == 200:
        max_ms = data['data']['ping_time_max']
        min_ms = data['data']['ping_time_min']
        return [max_ms,min_ms]
    else:
        return data['data']
