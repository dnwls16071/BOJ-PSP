# 알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 모음(a, e, i, o, u)의 개수를 출력하는 프로그램을 작성하시오.

word = input().lower()
vowel = ['a','e','i','o','u']

cnt = 0
for i in word:
    if i in vowel:
        cnt += 1
    else:
        cnt += 0
print(cnt)