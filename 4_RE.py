#정규식표현
#w3school, python re 페이지 등으로 추가적인 공부

import re
# ex) ca?e 로 구성된 문자
#. (ca.e): 하나의 문자 > care, cafe / caffe (x)
#^ (^de): 문자열의 시작 > desk, destiny / fade (x)
#$ (se$): 문자열의 끝 > case, base / face (x)

#match
p = re.compile("ca.e") 
m = p.match("caffee")
print(m.group()) #정규식과 매칭되면 그 값이 나오고 매치 안 되면 에러 발생

def print_match(m):
    if m:
     print("m.group(): ", m.group()) #일치하는 문자열 반환
     print("m.string: ", m.string) #입력받은 문자열, ()없이 입력하기!
     print("m.start(): ", m.start()) #일치하는 문자열 첫 index
     print("m.end(): ", m.end()) #일치하는 문자열 끝 index
     print("m.spen(): ", m.span()) #일치하는 문자열 시작과 끝 index
    else: 
        print("매칭되지 않음")

m = p.match("caffee") #match는 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)


#search
m = p.search("good care") #주어진 문자열 중에 일치하는지 확인
print_match(m)


#findall
lst = p.findall("careless cafe") #일치하는 모든 것을 리스트 형태로 반환
print(lst)

