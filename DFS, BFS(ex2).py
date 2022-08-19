# 동빈이는 N * M 크기의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리 괴물이 있어 이를 피해 탈출해야 합니다.
# 동빈이의 위치는 (1, 1)이며, 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다.
# 이때, 괴물이 있는 부분은 0으로 괴물이 없는 부분은 1로 표시되어 있습니다. 미로는 반드시 탈출할 수 있는 형태로 제시되어 있습니다.
# 이때, 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.(단, 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

from collections import deque

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치를 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or  nx >= N or ny < 0 or ny >= M:
                continue
            # 해당 노드가 괴물이 있는 곳이라면?
            if graph[nx][ny] == 0:
                continue
            # 해당 노드가 괴물이 없는 곳이라면?
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 바로 직전 노드위치에서의 최단거리값에 1을 증가
                queue.append((nx, ny))
    return graph[N-1][M-1]

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(BFS(0, 0))