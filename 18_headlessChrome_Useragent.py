#headless Chrome실행 시 문제점

from selenium import webdriver

#background에서 크롬 브라우저를 실행하기(option만 설정하면 됨)
options = webdriver.ChromeOptions()
options.headless = True
#백그라운드에서 크롬 활성화된 창 크기 설정
options.add_argument("window-size = 1920x1080")
#headless로 접속시 user-agent가 headless로 나오기 때문에 설정해주기
options.add_argument("user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")
browser = webdriver.Chrome(options = options)

browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
# "Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/85.0.4183.121 Safari/537.36"

print(detected_value.text)
browser.quit()