# 문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

# 1차 작성 코드
T = int(input())

for _ in range(T):
    sentence = list(input().split(" "))
    for i in sentence:
        print(i[::-1], end = " ")