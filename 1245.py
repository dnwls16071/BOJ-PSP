# 농부 민식이가 관리하는 농장은 N×M 격자로 이루어져 있다. 민식이는 농장을 관리하기 위해 산봉우리마다 경비원를 배치하려 한다. 이를 위해 농장에 산봉우리가 총 몇 개 있는지를 세는 것이 문제다.
#
# 산봉우리의 정의는 다음과 같다. 산봉우리는 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합으로 이루어져 있다. (여기서 "인접하다"의 정의는 X좌표 차이와 Y좌표 차이 모두 1 이하일 경우로 정의된다.) 또한 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야한다.
#
# 문제는 격자 내에 산봉우리의 개수가 총 몇 개인지 구하는 것이다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def DFS(x, y):
    global flag
    visited[x][y] = 1

    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, 1, 0, -1, -1, 1, -1, 1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[x][y] < graph[nx][ny]:
                flag = False
            if not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                DFS(nx, ny)

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
visited = [[0] * M for _ in range(N)]

flag = True
cnt = 0
for x in range(N):
    for y in range(M):
        if graph[x][y] > 0 and not visited[x][y]:
            flag = True
            DFS(x, y)
            if flag:
                cnt += 1
print(cnt)
