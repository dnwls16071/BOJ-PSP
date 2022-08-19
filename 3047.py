# 세 수 A, B, C가 주어진다. A는 B보다 작고, B는 C보다 작다.

# 세 수 A, B, C가 주어졌을 때, 입력에서 주어진 순서대로 출력하는 프로그램을 작성하시오.

num_list = list(map(int, input().split()))
word = input()
num = sorted(num_list)

for i in word:
    if i == "A":
        print(num[0], end = " ")
    elif i == "B":
        print(num[1], end = " ")
    elif i == "C":
        print(num[2], end = " ")
