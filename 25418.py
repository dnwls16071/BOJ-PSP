# 입력으로 양의 정수 A와 K가 주어지면, 아래 연산을 이용하여 A를 K로 변경하려고 한다. 정수 A를 변경할 때 사용할 수 있는 연산 종류는 다음과 같다.
#
# 연산 1: 정수 A에 1을 더한다.
# 연산 2: 정수 A에 2를 곱한다.
# 정수 A를 정수 K로 만들기 위해 필요한 최소 연산 횟수를 출력하자.

import sys
input = sys.stdin.readline
from collections import deque

def BFS(start):
    queue = deque()
    queue.append(start)

    while queue:
        x = queue.popleft()
        if x == K:
            return count[x]
        for nx in (x+1, x*2):
            if A <= nx <= 1000000 and not count[nx]:
                count[nx] = count[x] + 1
                queue.append(nx)

A, K = map(int, input().split())
count = [0] * 1000001
print(BFS(A))

# 숨바꼭질(1697번) 문제와 비슷한 유형의 문제였다.