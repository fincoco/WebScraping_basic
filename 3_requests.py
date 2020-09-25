!pip install requests

import requests
res = requests.get("http://google.com")
res2 = requests.get("http://fincoco.tistory.com")
res.raise_for_status() #웹스크래핑 위해 올바로 코드 가져오지 않으면 에러를 냄
res2.raise_for_status() 
#위 두줄로 html 소스를 제대로 가져왔는지 확인 가능

# print("응답코드: ", res.status_code) #코드가 200이면 접근 가능하다는 뜻. 정상
# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")
# res.raise_for_status() #웹스크래핑 위해 올바로 코드 가져오지 않으면 에러를 냄
# print("웹스크래핑을 진행합니다")

print(len(res.text))

with open("mygoogle.html", "w", encoding="utf8") as f: #html파일로 가져오기
    f.write(res.text)

