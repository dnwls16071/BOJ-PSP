# N(1 ≤ N ≤ 100,000)개의 정수들이 있을 때, a번째 정수부터 b번째 정수까지 중에서 제일 작은 정수, 또는 제일 큰 정수를 찾는 것은 어려운 일이 아니다. 하지만 이와 같은 a, b의 쌍이 M(1 ≤ M ≤ 100,000)개 주어졌을 때는 어려운 문제가 된다. 이 문제를 해결해 보자.
#
# 여기서 a번째라는 것은 입력되는 순서로 a번째라는 이야기이다. 예를 들어 a=1, b=3이라면 입력된 순서대로 1번, 2번, 3번 정수 중에서 최소, 최댓값을 찾아야 한다. 각각의 정수들은 1이상 1,000,000,000이하의 값을 갖는다.

import sys
N, M = map(int, sys.stdin.readline().split())
lst = []
for _ in range(N):
    lst.append(int(input()))

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    tmp = lst[a-1:b]
    min_val = min(tmp)
    max_val = max(tmp)
    print(min_val, max_val)
