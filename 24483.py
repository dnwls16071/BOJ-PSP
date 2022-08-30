# 오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
#
# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 깊이 우선 탐색으로 만들어 지는 트리를 깊이 우선 탐색 트리라고 하자. 깊이 우선 탐색 트리에 있는 i번 노드의 깊이(depth)를 di라고 하자. 시작 정점 R의 깊이는 0이고 방문 되지 않는 노드의 깊이는 -1이다. 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 i번 노드의 방문 순서를 ti라고 하자. 시작 정점의 방문 순서는 1이고 시작 정점에서 방문할 수 없는 노드는 0이다. 모든 노드에 대한 di × ti 값의 합을 구해보자.
#
# 깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.
#
# dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#         if (visited[x] = NO) then dfs(V, E, x);
# }

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)   # 방문 순서
node_visited = [-1] * (N+1) # 방문 여부
count = 1
total = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

def DFS(graph, start, visited):
    global count
    visited[start] = count
    for i in graph[start]:
        if not visited[i] and node_visited[i] == -1:
            node_visited[i] = node_visited[start] + 1
            count += 1
            DFS(graph, i, visited)

node_visited[R] = 0
DFS(graph, R, visited)
for i in range(1, N+1):
    total += visited[i] * node_visited[i]
print(total)

# 시작 정점 R의 깊이는 0이고 방문하지않은 노드의 깊이는 -1이라고 가정
# 시작 정점의 방문 순서는 1이고 시작 정점에서 방문할 수 없는 노드는 0이라고 가정
# 따라서 방문여부를 따지는 배열 하나와 방문순서를 따지는 배열 하나 총 두 개의 배열을 가지고 DFS를 진행하면된다.
# 오름차순 정렬