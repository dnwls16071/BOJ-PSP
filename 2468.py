# 재난방재청에서는 많은 비가 내리는 장마철에 대비해서 다음과 같은 일을 계획하고 있다. 먼저 어떤 지역의 높이 정보를 파악한다. 그 다음에 그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사하려고 한다. 이때, 문제를 간단하게 하기 위하여, 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.
#
# 어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수이다. 예를 들어, 다음은 N=5인 지역의 높이 정보이다.
#
# 6	8	2	6	2
# 3	2	3	4	6
# 6	7	3	3	2
# 7	2	5	3	6
# 8	9	5	2	7
# 이제 위와 같은 지역에 많은 비가 내려서 높이가 4 이하인 모든 지점이 물에 잠겼다고 하자. 이 경우에 물에 잠기는 지점을 회색으로 표시하면 다음과 같다.
#
# 6	8	2	6	2
# 3	2	3	4	6
# 6	7	3	3	2
# 7	2	5	3	6
# 8	9	5	2	7
# 물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역을 말한다. 위의 경우에서 물에 잠기지 않는 안전한 영역은 5개가 된다(꼭짓점으로만 붙어 있는 두 지점은 인접하지 않는다고 취급한다).
#
# 또한 위와 같은 지역에서 높이가 6이하인 지점을 모두 잠기게 만드는 많은 비가 내리면 물에 잠기지 않는 안전한 영역은 아래 그림에서와 같이 네 개가 됨을 확인할 수 있다.
#
# 6	8	2	6	2
# 3	2	3	4	6
# 6	7	3	3	2
# 7	2	5	3	6
# 8	9	5	2	7
# 이와 같이 장마철에 내리는 비의 양에 따라서 물에 잠기지 않는 안전한 영역의 개수는 다르게 된다. 위의 예와 같은 지역에서 내리는 비의 양에 따른 모든 경우를 다 조사해 보면 물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5임을 알 수 있다.
#
# 어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

Maximum = 0
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if graph[i][j] > Maximum:
            Maximum = graph[i][j]

def BFS(a, b, height):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > height and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

result = 0
for i in range(Maximum):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if graph[x][y] > i and visited[x][y] == 0:
                BFS(x, y, i)
                cnt += 1
    if result < cnt:
        result = cnt
print(result)

# 각 지역 높이의 최댓값만큼 for문을 돌려 안전영역 개수의 최댓값을 찾는다.
# 만약 내리는 비의 양보다 지역의 높이가 더 높고 방문하지않았다면 BFS를 계속 돌리면서 개수를 증가시킨다.
