# 해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
#
# 이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
#
# 이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
from collections import deque

def BFS(v):
    queue = deque()
    queue.append(v)
    visited = [0] * (N+1)
    visited[v] = 1
    cnt = 1

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
                cnt += 1
    return cnt

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

result = []
for i in range(1, N+1):
    result.append(BFS(i))

max = max(result)
for i in range(len(result)):
    if result[i] == max:
        print(i+1, end = " ")

# 문제를 이해하면 다음과 같다.
# 예를 들어 1 2인 경우 2번 컴퓨터를 해킹했을때 1번 컴퓨터도 같이 해킹이 된다는 뜻이다.
# 따라서 graph[B].append(A) 단방향으로 연결이 성립된다.

# 이번 문제는 입력받는 간선 정보가 양방향이 아니라 단방향이다. 그 점만 주의하면 될 거 같다.

# 1번 컴퓨터를 해킹했을때 3번 컴퓨터도 같이 해킹이 된다.
# 2번 컴퓨터를 해킹했을때 3번 컴퓨터도 같이 해킹이 된다.
# 3번 컴퓨터를 해킹했을때 4번 컴퓨터도 같이 해킹이 된다.
# 3번 컴퓨터를 해킹했을때 5번 컴퓨터도 같이 해킹이 된다.
# 따라서 graph를 확인해보면 다음과 같다.
# [[], [3], [3], [4, 5], [], []]