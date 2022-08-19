# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

N = int(input())

word = []
for i in range(N):
    word.append(input())

word = list(set(word))  # 같은 단어가 여러 번 입력된 경우 집합으로 통일
# (key = lambda 인자 : (정렬기준))
word.sort(key=lambda x : (len(x), x))

for i in word:
    print(i)





