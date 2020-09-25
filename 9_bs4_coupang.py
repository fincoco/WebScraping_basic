#http method: 
# get(url을 통해, ?와 &로 연결해서 변수와 값을 보냄), 한번에 보낼 수 있는 양이 정해져있음
# post(http 메세지 바디 안에 보안방식으로, url이 변하지 않음), 크기가 큰 파일도 보낼 수 있음

#쿠팡에서 웹스크래핑하기
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs = {"class" : re.compile("^search-product")})
print(items[0].find("div", attrs = {"class" : "name"}).get_text())

#평점 혹은 리뷰 없는 경우 if문으로 처리
for item in items:
    #광고제품 제외하고 다음으로 넘어가기
    ad_badge = item.find("span", attrs = {"class" : "ad-badge-text"})
    if ad_badge:
        print("    < 광고 상품 제외합니다 >")
        continue

    name = item.find("div", attrs = {"class" : "name"}).get_text()
    #애플제품 제외하기
    if "Apple" in name: 
        print("    < 애플 상품 제외합니다 >")
        continue
    price = item.find("strong", attrs = {"class" : "price-value"}).get_text()
    
    #리뷰 50개 이상, 펴점 4.5 이상 제품만 조회
    rate = item.find("em", attrs = {"class" : "rating"})
    if rate:
        rate = rate.get_text() 
    else:
        print("    < 평점 없는 상품 제외합니다 >")
        continue

    review = item.find("span", attrs = {"class" : "rating-total-count"})
    if review:
        review = review.get_text()
        review = review[1:-1] #() 빼고 슬라이싱

    else:
        print("    < 리뷰 없는 상품 제외합니다 >")
        continue

    if float(rate) >= 4.5 and int(review) >= 50:
        print(name, price, rate, review)

