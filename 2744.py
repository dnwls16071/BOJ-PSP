# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.

word = list(str(input()))
answer = [] # answer 리스트 생성

for i in word:  # word를 이루는 문자 하나하나를 받아옴
    if i in "abcdefghijklmnopqrstuvwxyz":   # 만약 i가 소문자에 해당한다면
        answer.append(i.upper())    # i를 대문자로 바꾸어 추가
    else:   # 만약 i가 대문자라면?
        answer.append(i.lower())    # i를 소문자로 바꾸어 추가

for i in answer:    
    print(i, end = "")
    