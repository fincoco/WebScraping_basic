#구글 무비 인기 차트 내에서 할인하는 영화 스크래핑(페이지 한글로 가져오기)

import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36", 
    "Accept-Language" : "ko-KR, ko" #한글페이지로 반환해달라고 요청, request로 접속하면 영어페이지 인식
    }

res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs = {"class" : "ImZGtf mpg5gc"})

# print(len(movies)) #10개만 출력, 스크롤할 때마다 추가로 로딩하는 동적 페이지이기 때문.
# with open("movie.html", "w", encoding = "utf8") as f:
#     f.write(soup.prettify()) #html 문서를 깔끔하게 출력

for movie in movies:
    title = movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text()
    print(title)