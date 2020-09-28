#동적 웹 스크래핑
#구글 무비 인기 차트 내에서 할인하는 영화 스크래핑(headless로 실행하기)

import requests, time
from bs4 import BeautifulSoup
from selenium import webdriver

#background에서 크롬 브라우저를 실행하기(option만 설정하면 됨)
options = webdriver.ChromeOptions()
options.headless = True
#백그라운드에서 크롬 활성화된 창 크기 설정
options.add_argument("window-size = 1920x1080")
browser = webdriver.Chrome(options = options)

browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

interval = 2 
prev_height = browser.execute_script("return document.body.scrollHeight") 

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
    time.sleep(interval) 
    curr_height = browser.execute_script("return document.body.scrollHeight") 
    
    if curr_height == prev_height: break
    prev_height = curr_height 

browser.get_screenshot_as_file("google_movie.png")

soup = BeautifulSoup(browser.page_source, "lxml") 
movies = soup.find_all("div", attrs = {"class" : "Vpfmgd"}) 

for movie in movies:
    title = movie.find("div", attrs = {"class" : "WsMG1c nnK0zc"}).get_text()
    original_price = movie.find("span", attrs = {"class" : "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else: continue 
    price = movie.find("span", attrs = {"class" : "VfPpfd ZdBevf i5DZme"}).get_text()
    link = movie.find("a", attrs = {"class" : "JC71ub"})["href"]
    
    print(f"제목: {title}")
    print(f"할인 전 금액: {original_price}")
    print(f"할인 된 금액: {price}")
    print("링크: ", "https://play.google.com" + link)
    print("-"*100)

browser.quit
    




