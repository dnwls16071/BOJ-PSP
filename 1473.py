# N×M크기의 배열로 표현되는 미로가 있다.
#
# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
#
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

from collections import deque

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 영역 외의 노드라면? => 그냥 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 이동할 수 없는 노드라면? => 그냥 무시
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N-1][M-1]

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(BFS(0, 0))

# [이것이 코딩테스트다 With 파이썬] 나동빈 유튜브 강의를 시청한 다음 문제를 풀어봤는데 확실히 이해가 되는 것 같았다.
# 고난도 문제에 바로 도전하기가 좀 부담스럽지만 DFS,BFS 실버 문제부터 차근차근 도전해봐야겠다.