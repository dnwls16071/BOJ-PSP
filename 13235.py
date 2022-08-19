# 팰린드롬은 앞에서부터 읽을 때와 뒤에서부터 읽을 때가 똑같은 단어를 의미한다. 예를 들어, eve, eevee는 팰린드롬이고, eeve는 팰린드롬이 아니다. 단어가 주어졌을 때, 팰린드롬인지 아닌지 판단해보자.

word = input()

if word == word[::-1]:
    print("true")
else:
    print("false")