# 코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다. 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다. 이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다.
#
# 이 문제를 출제한 선생님은 개인적으로 이러한 음식물을 실내화에 묻히는 것을 정말 진정으로 싫어한다. 참고로 우리가 구해야 할 답은 이 문제를 낸 조교를 맞추는 것이 아니다.
#
# 통로에 떨어진 음식물을 피해가기란 쉬운 일이 아니다. 따라서 선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다.
#
# 선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.

from collections import deque

def BFS(x, y):
    cnt = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 해당 노드의 값이 1인 경우 => 음식물 쓰레기가 있는 곳
            if 0 <= nx < N and 0 <= ny < M and place[nx][ny] == 1 and not visited[nx][ny]:
                # 해당 노드 방문 처리
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1
    return cnt+1


N, M, K = map(int, input().split())
place = [[0] * (M) for _ in range(N)]   # 2차원 배열 통로
visited = [[False] * (M) for _ in range(N)]   # 2차원 배열 방문
for _ in range(K):
    a, b = map(int, input().split())
    place[a-1][b-1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_val = 0
for a in range(N):
    for b in range(M):
        # 해당 노드의 값이 1(음식물 쓰레기가 있는 노드)이면서 방문을 하지 않았다면?
        if place[a][b] == 1 and not visited[a][b]:
            # BFS를 실행
            max_val = max(max_val, BFS(a, b))
print(max_val)