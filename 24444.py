# 오늘도 서준이는 너비 우선 탐색(BFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
#
# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.
#
# 너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.
#
# bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     for each v ∈ V - {R}
#         visited[v] <- NO;
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
#     while (Q ≠ ∅) {
#         u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
#         for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#             if (visited[v] = NO) then {
#                 visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
#                 enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
#             }
#     }
# }

import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
count = 1

# 입력받는 간선 정보들을 그래프화
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 각 간선 정보들을 정렬
for i in range(N+1):
    graph[i].sort()

def BFS(graph, start, visited):
    global count
    queue = deque([start])
    visited[start] = 1
    while queue:
        start = queue.popleft()
        for i in graph[start]:
            if visited[i] == 0:
                count += 1
                queue.append(i)
                visited[i] = count

BFS(graph, R, visited)
for i in visited[1:]:
    print(i)

# BFS => from collections import deque 필수
# visited 배열은 방문여부를 확인하기 위해 만든 배열
# 오름차순/내림차순 정렬
# 입력받는 간선 정보들을 빈 종이에 그려 그래프화하고 배열 추가하는 방법을 이용해 각 정점으로부터 연결된 정점들을 추가
# 방문하지않은 노드는 0, 방문한 노드는 1로 처리
