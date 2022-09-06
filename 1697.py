# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
#
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오

import sys
input = sys.stdin.readline
from collections import deque

def BFS(start):
    queue = deque()
    queue.append(start)

    while queue:
        x = queue.popleft()
        if x == K:
            print(count[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and not count[nx]:
                count[nx] = count[x] + 1
                queue.append(nx)

N, K = map(int, input().split())
count = [0] * 100001
BFS(N)

# 계속 WA판정을 받아서 어디가 문제인지 판단하기 힘들었다.
# 점 N, K의 최댓값은 100000이라는 조건을 참고해서 작성해야한다.
