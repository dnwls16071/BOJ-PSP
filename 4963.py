# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
#
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
#
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

import sys
sys.setrecursionlimit(10000)
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

def DFS(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            graph[nx][ny] = 0
            DFS(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    result = 0
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    for a in range(h):
        for b in range(w):
            if graph[a][b] == 1:
                result += 1
                DFS(a, b)
    print(result)

# 재귀 호출을 이용하는 경우 가끔 RecursionError(재귀에러)를 호출할 수 있다.
# 이는 재귀 최대 깊이를 초과하기 때문에 나타나는 자연적인 현상이므로 이를 해결하기 위해서 재귀 최대 깊이를 제한하는 코드를 작성할 수 있다.

# import sys
# sys.setrecursionlimit(10000)  => 재귀를 사용해서 풀어야 하는 문제라면, 이 코드문은 필수로 작성해야 한다.