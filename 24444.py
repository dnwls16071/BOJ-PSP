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

# BFS가 무슨 내용인지 알 수 있었던 좋은 문제였다.
# BFS(Breadth First Search) 그래프 이론의 핵심 정리
# BFS를 구현할때에는 from collections import deque를 사용해서 큐를 구현한다.
# graph를 만들때는 2차원 배열로 0번째 값을 고려해서 한 개 더 만든다.
# 입력받는 간선 정보들을 그래프화하는 작업을 거친다.
# 빈 종이에 간선 정보들을 그래프화하여 그린 다음 작업을 진행했더니 훨씬 더 수월했다.
# 각 간선 정보들을 오름차순/내림차순 정렬해준다.
