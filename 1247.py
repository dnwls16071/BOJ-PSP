# N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
for _ in range(3):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(int(input()))
    if sum(lst) > 0:
        print("+")
    elif sum(lst) < 0:
        print("-")
    else:
        print(0)