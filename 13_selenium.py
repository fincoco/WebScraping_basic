#클릭, 글자 입력 등 가능하게 하는 프레임워크
#chromedriver 다운로드 필요

from selenium import webdriver

browser = webdriver.Chrome() #"./chromedriver.exe" 경로 정보 
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.back()
# browser.forward()
# browser.refresh() #새로고침

elem2 = browser.find_element_by_id("query")
elem2.send_keys("나도코딩")
from selenium.webdriver.common.keys import Keys
elem2.send_keys(Keys.ENTER) #엔터키 누를 때 import먼저 하고!

elem3 = browser.find_element_by_tag_name("a")
elem4 = browser.find_elements_by_tag_name("a") #element 전체 가져오기, a tag 전체
for e in elem4:
    e.get_attribute("href")

browser.get("http://daum.net") #홈페이지 이동
elem = browser.find_element_by_name("q")
elem.send_keys("나도코딩")
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()

browser.close() #열려있는 탭 닫기
browser.quit() #모든 브라우저 닫기


#네이버 로그인하기
import time
from selenium import webdriver

browser = webdriver.Chrome() 
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

#id, pw 입력하기(잘못된 입력)
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

browser.find_element_by_id("log.login").click()

#id, pw 새로 입력
# time.sleep(3)
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys("my_id")

#html 정보 출력
print(browser.page_source) #페이지에 있는 브라우저 정보 가져오기
browser.quit()

