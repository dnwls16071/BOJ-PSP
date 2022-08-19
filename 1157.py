# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 형 변환(list형으로 바꾼 뒤에 set형으로 바꾸나, set형으로 바꾼 뒤에 list형으로 바꾸나 결과에 차이는 없다)
# 하지만 결과값의 형식에는 집합이냐 리스트이냐의 차이를 보인다.

word = input().upper()
word_list = list(set(word))

cnt = []
count = 0
for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[cnt.index(max(cnt))])
