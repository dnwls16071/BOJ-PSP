# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
#
# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
#
# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**2)

R, C = map(int, input().split())
visited = []
graph = []
for _ in range(R):
    graph.append(list(input()))

ans = 0
def DFS(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 안에 있으면서 그래프를 순회했을때 만약에 방문했던 노드 알파벳이 업다면?
        if 0 <= nx < R and 0 <= ny < C and not graph[nx][ny] in visited:
            # 말 추가
            visited.append(graph[nx][ny])
            DFS(nx, ny, cnt+1)
            visited.remove(graph[nx][ny])
    return
# 좌측 상단 칸에 있는 말을 추가
visited.append(graph[0][0])
DFS(0, 0, 1)
print(ans)

# 계속 메모리 초과가 나와서 어디가 문제인지 알 수 없어 많이 헤맸던 문제였다.
# 재귀깊이를 작은 값으로 설정해줬더니 통과되었다.

# 이 문제를 통해서 한 가지 중요한 사실을 알게 되었다.
# 집합과 리스트의 차이를 정리하면 집합은 중복되는 인자를 가지지 않는다는 것이고 리스트는 중복되는 인자를 가진다.
# 리스트를 사용하는 경우의 시간복잡도와 집합을 사용하는 경우의 시간복잡도는 다르다.
# 중복되는 숫자가 많을수록 시간복잡도가 감소하므로 숫자의 중복성이 보인다면 집합을 사용하는 편이 좋다.
