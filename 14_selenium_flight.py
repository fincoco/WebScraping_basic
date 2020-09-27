from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

#가는날 선택
browser.find_element_by_link_text("가는날 선택").click()

#이번달 29, 30일 선택
# browser.find_elements_by_link_text("29")[0].click() #28 전체 찾고 가장 첫번째 것 선택
# browser.find_elements_by_link_text("30")[0].click()

#다음달 29, 30일 선택
# browser.find_elements_by_link_text("29")[1].click() 
# browser.find_elements_by_link_text("30")[1].click()

#이번달 29, 다음달 30일
browser.find_elements_by_link_text("29")[0].click() 
browser.find_elements_by_link_text("30")[1].click()

#제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

#로딩 시간 미리 설정하기 
#최대 10초로 어떤 elem이 나올 때 까지 기다리기
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")) 
    print(elem.text) #10초 이상 걸리면 종료시키기 
finally:
    browser.quit()

#첫번째 결과 출력
elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
