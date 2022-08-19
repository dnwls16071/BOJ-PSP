# 음료수 얼려 먹기: 문제 설명

# N * M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시합니다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되는 것으로 간주합니다.
# 이때, 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
# 다음은 4 * 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.

# DFS로 특정 노드를 방문하고 상,하,좌,우로 연결된 노드들을 방문한다.
def DFS(x, y):
    # 주어진 범위를 벗어나는 경우는 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 현재 노드를 방문하지 않았다면? => 즉, 얼음판에서 구멍이 뚫려있는 부분이라면?
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리
        graph[x][y] = 1
        # 상,하,좌,우 위치들을 재귀 호출
        DFS(x, y+1)
        DFS(x-1, y)
        DFS(x, y-1)
        DFS(x+1, y)
        return True
    return False

# N, M을 공백을 기준으로 구분하여 입력하기
N, M = map(int, input().split())

# 2차원 리스트 얼음틀 정보 입력 받기
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 모든 노드에 대하여 DFS를 수행
result = 0
for i in range(N):
    for j in range(M):
        # DFS수행하여 True가 반환된다면? => 아이스크림 개수 증가
        if DFS(i, j):
            result += 1

print(result)