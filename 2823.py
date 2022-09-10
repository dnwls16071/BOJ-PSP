# 상근이는 여자친구와의 드라이브를 위해서 운전을 배우고 있다. 도로 연수를 10년쯤 하다 보니 운전은 그럭저럭 잘하게 되었다. 하지만, 그는 유턴을 하지 못한다. 10년동안 도로 연수를 받았지만 유턴을 하지 못한다. 밥먹고 유턴만 연습했지만, 결국 유턴은 하지 못했다.
#
# 상근이는 유턴을 연습하기 위해서 시간을 투자하는 대신에 유턴을 할 필요가 없고, 유턴이 금지된 마을로 이사가려고 한다.
#
#
#
# 상근이가 이사가려고 하는 마을은 막다른 길이 있으면 안 된다. 막다른 길은 유턴을 하지 않고는 빠져나올 수 없기 때문이다. 어떤 마을의 지도가 주어졌을 때, 유턴을 하지 않고 마을의 모든 구역을 돌아다닐 수 있는지 없는지(막다른 길이 있는지 없는지)를 구하는 프로그램을 작성하시오.
#
# 마을의 지도는 R × C 칸으로 이루어진 표로 생각할 수 있다. 각 칸에 빌딩이 있다면 'X'로 표시하고, 길이라면 '.'으로 표시한다. 모든 칸은 빌딩 또는 길이다. 상근이가 어떤 길 위에 있다면, 근처 네 방향(위,아래,오른쪽,왼쪽)의 길로 이동할 수 있다. 빌딩으로는 이동할 수 없다.
#
# 이 마을에 막다른 길이 없다면, 상근이는 임의의 한 길에서 시작해서, 갈 수 있는 어떤 방향으로 움직이더라도, 유턴을 하지 않고 그 위치로 돌아올 수 있어야 한다.
#
# 유턴은 방금 이동한 방향의 반대 방향으로 이동하는 것을 말한다.

import sys
input = sys.stdin.readline
from collections import deque

def BFS(v):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([])
    queue.append(v)
    while queue:
        x, y = queue.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == ".":
                cnt += 1
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
        if cnt < 2:
            return 1
    return 0

check = []
R, C = map(int, input().split())
graph = []
for i in range(R):
    graph.append(list(map(str, input())))
    for j in range(C):
        if graph[i][j] == ".":
            check.append([i, j])

visited = [[0] * C for _ in range(R)]
print(BFS(check[0]))