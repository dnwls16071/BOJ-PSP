# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 배열형식으로 풀라고 지시하는 문제

import sys
input = sys.stdin.readline

N = int(input())

num = [0] * 10001

for _ in range(N):
    temp = int(input())
    num[temp] += 1

for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)