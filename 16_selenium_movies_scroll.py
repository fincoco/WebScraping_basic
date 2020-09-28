#동적 웹 스크래핑
#구글 무비 인기 차트 내에서 할인하는 영화 스크래핑(페이지 로딩)

import requests, time
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

#지정한 위치로 스크롤 내리기(java script 사용한 것)
# browser.execute_script("window.scrollTo(0, 1080)") #세로방향으로 1080 위치로 스크롤 내리기(한 페이지)
#화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") #현재 문서의 높이만큼 스크롤 내리기

interval = 2 
prev_height = browser.execute_script("return document.body.scrollHeight") #현재 문서 높이 가져오기

while True:
    #스크롤 가장 아래로 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
    #페이지 로딩 대기
    time.sleep(interval) #2초에 한번 스크롤 내림
    #현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight") 
    
    if curr_height == prev_height: break

    #현재 높이 다시 업데이트
    prev_height = curr_height 

soup = BeautifulSoup(browser.page_source, "lxml") #스크롤을 모두 내린 browser정보 가져오기
movies = soup.find_all("div", attrs = {"class" : "Vpfmgd"}) #div 클래스 이름이 여러가지 인 경우

#인기차트 200개 전체 가져오기
# for movie in movies:
#     title = movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text()
#     print(title)

for movie in movies:
    title = movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text()
    #할인 전 가격
    original_price = movie.find("span", attrs = {"class" : "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else: 
        # print(title, "<할인되지 않은 영화 제외>")
        continue
    
    #할인 된 가격
    price = movie.find("span", attrs = {"class" : "VfPpfd ZdBevf i5DZme"}).get_text()

    #링크
    link = movie.find("a", attrs = {"class" : "JC71ub"})["href"]
    
    print(f"제목: {title}")
    print(f"할인 전 금액: {original_price}")
    print(f"할인 된 금액: {price}")
    print("링크: ", "https://play.google.com" + link)
    print("-"*100)

browser.quit
    




