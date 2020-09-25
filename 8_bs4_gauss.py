import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status() #제대로 가져왔는지 확인
soup = BeautifulSoup(res.text, "lxml") 

#네이버 웹툰
#제목과 링크 스크래핑
cartoons = soup.find_all("td", attrs = {"class" : "title"})
title = cartoons[0].a.get_text()
link = cartoons[0].a["href"]
print(title)
print("https://comic.naver.com"+link)

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com"+cartoon.a["href"]
    print(title, link)


#평점 정보 스크래핑
total_rates = 0
cartoons = soup.find_all("div", attrs = {"class" : "rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수: ", total_rates)
print("평균 점수: ", total_rates/len(cartoons))