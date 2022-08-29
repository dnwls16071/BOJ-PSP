import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

def DFS(graph, start, visited):
    for i in graph[start]:
        if visited[i] == -1:
            visited[i] = visited[start] + 1
            DFS(graph, i, visited)

visited[R] = 0
DFS(graph, R, visited)
for i in range(1, N+1):
    print(visited[i])

# 24479번 문제와 동일한 유형
# 방문하지않은 노드를 -1로 처리