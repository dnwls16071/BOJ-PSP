# BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.
#
# 오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.
#
# A는 B와 친구다.
# B는 C와 친구다.
# C는 D와 친구다.
# D는 E와 친구다.
# 위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [0] * N
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(idx, depth):
    visited[idx] = 1
    # 친구 관계가 존재한다면 1을 출력
    if depth == 4:
        print(1)
        exit(0)
    for i in graph[idx]:
        if not visited[i]:
            visited[i] = 1
            DFS(i, depth+1)
            visited[i] = 0

for i in range(N):
    DFS(i, 0)
    visited[i] = 0
# 만약 친구 관계가 존재하지 않는다면 0을 출력
print(0)
