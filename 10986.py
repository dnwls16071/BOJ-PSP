# 수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
#
# 즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

from itertools import accumulate

N, M = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
for i in lst:
    if i % M == 0:
        cnt += 1

for i in range(N-2):
    lst = list(accumulate(lst))
    for j in lst:
        if j % M == 0:
            cnt += 1