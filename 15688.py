# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이며, 같은 수가 여러 번 중복될 수도 있다.

import sys

N = int(sys.stdin.readline())

num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()

for i in num_list:
    print(i)