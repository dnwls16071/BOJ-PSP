import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())
visited = [-1] * (N+1)
graph = [[] for _ in range(N+1)]

# 입력받는 간선 정보들을 그래프화
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 각 간선 정보들을 정렬
for i in range(N+1):
    graph[i].sort()

def BFS(graph, start, visited):
    queue = deque([start])
    while queue:
        start = queue.popleft()
        for i in graph[start]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[start] + 1

visited[R] = 0
BFS(graph, R, visited)
for i in visited[1:]:
    print(i)

# 24444번 문제와 동일한 유형
# 방문하지않은 노드를 -1로 처리