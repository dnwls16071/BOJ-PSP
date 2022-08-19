# 세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.
#
# N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램을 작성하시오.

from itertools import combinations

N, C = map(int, input().split())
weight = list(map(int, input().split()))

cnt = 1 # 아무것도 안 넣는 경우도 가능하므로 1로 지정
for i in range(1, N+1):
    for t in combinations(weight, i):
        if sum(t) <= C:
            cnt += 1
print(cnt)
