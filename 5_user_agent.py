#접속하는 서버에 따라 user agent가 달라짐.
#접속할 크롬 내의 내 유저 에이전트 설정 후 웹스크래핑 해야 정확한 정보 가져올 수 있음.

import requests

url = "http://nadocoding.tistory.com"
headers = {User Agent":Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36}
res = requests.get(url, headers = headers)
res.raise_for_status() 

with open("nadocoding.html", "w", encoding="utf8") as f: 
    f.write(res.text)


