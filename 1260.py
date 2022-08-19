# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

from collections import deque

def DFS(n):
    visited[n] = True
    print(n, end = " ")
    for i in graph[n]:
        if not visited[i]:
            DFS(i)

def BFS(n):
    queue = deque([n])
    visited[n] = True
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]    # 정점 개수만큼 반복
for i in range(M):  # 간선 개수만큼 반복
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)

DFS(V)

print()

visited = [False] * (N+1)

BFS(V)

# 유튜브애 나와있는 DFS, BFS 알고리즘 강의를 듣고 이해하고 처음 도전해본 문제였는데 아직까지도 많이 기본기가 부족하다는 것을 느꼈다.
# BFS/DFS 알고리즘은 코딩테스트에서 자주 나오는 유형이므로 반드시 이해해야하는것이 필수다.
# BFS/DFS 두 번 거쳐야하므로 방문 처리 여부를 나타내는 배열을 따로 두 번 선언해서 결과를 확인해야한다.
