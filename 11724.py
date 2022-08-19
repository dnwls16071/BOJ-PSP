# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

def DFS(lst, v, visited):
    visited[v] = True
    for i in lst[v]:
        if not visited[i]:
            DFS(lst, i, visited)

visited = [False] * (N+1)
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        if not lst[i]:
            cnt += 1
            visited[i] = True
        else:
            DFS(lst, v)