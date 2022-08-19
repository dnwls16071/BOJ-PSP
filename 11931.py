# N개의 수가 주어졌을 때, 이를 내림차순으로 정렬하는 프로그램을 작성하시오.

import sys

N = int(sys.stdin.readline())

num_lst = []
for _ in range(N):
    num_lst.append(int(sys.stdin.readline()))
num_lst.sort(reverse=True)

for i in num_lst:
    print(i)