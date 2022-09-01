# 보물섬 지도를 발견한 후크 선장은 보물을 찾아나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다. 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다.
#
# 예를 들어 위와 같이 지도가 주어졌다면 보물은 아래 표시된 두 곳에 묻혀 있게 되고, 이 둘 사이의 최단 거리로 이동하는 시간은 8시간이 된다.
#
# 보물 지도가 주어질 때, 보물이 묻혀 있는 두 곳 간의 최단 거리로 이동하는 시간을 구하는 프로그램을 작성하시오.

from collections import deque

L, W = map(int, input().split())

graph = []
for _ in range(L):
    graph.append(list(input().rstrip()))

def BFS(x, y):
    global distance
    queue = deque()
    queue.append((x, y))
    visited = [[0] * W for _ in range(L)]
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= L or ny < 0 or ny >= W:
                continue
            elif 0 <= nx < L and 0 <= ny < W and visited[nx][ny] == 0 and graph[nx][ny] == "L":
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                distance = max(distance, visited[nx][ny])
    return distance - 1

distance = 0
result = 0
for x in range(L):
    for y in range(W):
        if graph[x][y] == "L":
            result = max(result, BFS(x, y))
print(result)

# 최단거리 문제이므로 바로 BFS를 떠올렸다.
# 육지인 L을 지나갈때마다 이동거리를 1씩 증가시켜 이동거리를 반환한다.
# 배열의 가로세로 값을 반대로 써서 어이없게 자꾸 틀렸다.