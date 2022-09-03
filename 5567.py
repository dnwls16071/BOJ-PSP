# 상근이는 자신의 결혼식에 학교 동기 중 자신의 친구와 친구의 친구를 초대하기로 했다. 상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지이다. 상근이의 학번은 1이다.
#
# 상근이는 동기들의 친구 관계를 모두 조사한 리스트를 가지고 있다. 이 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
from collections import deque

def BFS(start):
    global cnt
    queue = deque()
    queue.append((start, 0))
    visited[start] = 1

    while queue:
        number, distance = queue.popleft()
        if distance <= 2:
            cnt += 1
        for i in graph[number]:
            if not visited[i]:
                visited[i] = 1
                queue.append((i, distance + 1))
    return cnt - 1

cnt = 0
n = int(input())
m = int(input())
visited = [0 for _ in range(n + 1)]
graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(BFS(1))

# 마지노선 범위는 상근이의 친구의 친구까지 결혼식에 초대할 수 있다.
# 족보상에서 거리가 2이하인 사람들은 초대할 수 있고 distance가 0일때 상근이가 포함되므로 상근이 본인은 빼야한다.

