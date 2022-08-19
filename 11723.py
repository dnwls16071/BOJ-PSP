# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
#
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

import sys
input = sys.stdin.readline

S = set()
M = int(input())
for _ in range(M):
    operation = input().strip().split()
    if len(operation) == 1: # 만약 명령어만 있고 숫자는 없는 경우
        if operation[0] == "all":
            S = set(range(1, 21))
        elif operation[0] == "empty":
            S = set()
    else:
        if operation[0] == "add":
            if int(operation[1]) in S:
                continue
            else:
                S.add(int(operation[1]))
        elif operation[0] == "remove":
            if int(operation[1]) not in S:
                continue
            else:
                S.remove(int(operation[1]))
        elif operation[0] == "check":
            if int(operation[1]) in S:
                print(1)
            else:
                print(0)
        elif operation[0] == "toggle":
            if int(operation[1]) in S:
                S.remove(int(operation[1]))
            else:
                S.add(int(operation[1]))

# 위 코드를 PyPy3로 제출했을때는 메모리 초과가 나왔고 Python3에서는 통과되었다.
# 입력값을 빠르게 받아오기 위해서 sys 라이브러리를 사용해야했다.
# 다른 자료형 문제와는 다르게 한 번에 입력하고 슬라이싱 기능을 이용했다.

# ex. operation = input().strip().split() => 이번 문제
# ex. operation, num = input().split() => 다른 문제