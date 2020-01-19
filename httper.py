import requests


# 使用requests库进行get请求发送

class HTTP:
    @classmethod
    def get(cls, url, return_json=True):
        r = requests.get(url)
        print(r.headers)
        if return_json:
            return r.json()
        else:
            return r.text
