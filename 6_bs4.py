# pip install bequtifulsoup4
# pip install lxml 

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() #제대로 가져왔는지 확인

soup = BeautifulSoup(res.text, "lxml") #lxml 파서
print(soup.title) #네이버 만화 &gt; 요일별  웹툰 &gt; 전체웹툰
print(soup.title.get_text()) #네이버 만화 > 요일별  웹툰 > 전체웹툰
print(soup.a) #첫번째로 발견되는 a element 정보가 출력(메인 메뉴 바로가기)
print(soup.a.attrs) #a element 가진 속성이 사전 형태로 출력
print(soup.a["href"]) #속성 중 href에 해당하는 value 출력

#일반적으로 웹스크래핑하는 대상 페이지 잘 모를 때는?
print(soup.find("a", attrs={"class" : "Nbtn_upload"})) #처음으로 발견되는 a element에서 속성이 class인 것 중 값이 ""인 것 찾기
print(soup.find(attrs={"class" : "Nbtn_upload"})) #'웹툰 올리기'버튼이 하나인 경우에는 속성만 지정해도 됨

#웹툰 랭킹 정보 가져오기
print(soup.find("li", attrs={"class" : "rank01"}))
rank1 = soup.find("li", attrs={"class" : "rank01"})
print(rank1.a) #a element만 출력 가능

#형제, 부모 element로 넘어가가
print(rank1.a.get_text()) #텍스트만 가져오는 경우
rank2 = rank1.next_sibling.next_sibling #다음 형제, 태그 사이에 줄바꿈 있는 경우 두 번 헤줘야 출력
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling #이전 형제
print(rank2.a.get_text())
print(rank1.parent.get_text())

#태그 간 개행 상관 없이 출력
rank2 = rank1.find_next_sibling("li") #li element기준으로 다음 형제 찾기
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())
rank2 = rank3.previous_sibling("li")

#랭킹 한번에 가져오기
rankall = rank1.find_next_siblings("li") #sibling 전체 가져오기
print(rankall)

#text로 가져오기
webtoon = soup.find("a", text = "갓 오브 하이스쿨-481화")
print(webtoon)

