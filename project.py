#pip install requests
#pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import re

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

#날씨 정보 가져오기
def scrape_weather():
    url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)

    cast = soup.find("p", attrs = {"class" : "cast_txt"}).get_text()

    curr_temp = soup.find("p", attrs = {"class" : "info_temperature"}).get_text().replace("도씨", "")
    min_temp = soup.find("span", attrs = {"class" : "min"}).get_text()
    max_temp = soup.find("span", attrs = {"class" : "max"}).get_text()
    
    morning_rain_rate = soup.find("span", attrs = {"class" : "point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs = {"class" : "point_time afternoon"}).get_text().strip()
    
    dust = soup.find("dl", attrs = {"class" : "indicator"})
    pm10 = dust.find_all("dd")[0].get_text()
    pm25 = dust.find_all("dd")[1].get_text()


    print("[오늘의 날씨]")
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()


#헤드라인 뉴스
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs = {"class" : "hdline_article_list"}).find_all("li", limit=3) #찾는 tag개수 설정
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print("  (링크: {}".format(link))
        print()

#IT뉴스
def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs = {"class" : "type06_headline"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 #img태그가 있으면 1번째 img태그 정보 사용
        title = news.find_all("a")[a_idx].get_text().strip() #이미지 있으면 두번째, 이미지 없으면 첫번째 정보 가져오기
        link = news.find_all("a")[a_idx]["href"]
        print("{}. {}".format(index+1, title))
        print("  (링크: {}".format(link))
        print()

#해커스 영어회화
def scrape_english():
    print("[오늘의 영어회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"
    soup = create_soup(url)

    sentences = soup.find_all("div", attrs = {"id" : re.compile("^conv_kor_t")})
    print("<영어 지문>")
    for sent in sentences[len(sentences)//2:]: 
        print(sent.get_text().strip())
    print()
    print("<한글 지문>")
    for sent in sentences[:len(sentences)//2]: 
        print(sent.get_text().strip())


if __name__ == "__main__": #직접 실행할 때만 
    scrape_weather() 
    scrape_headline_news()
    print()
    scrape_it_news()
    scrape_english()


