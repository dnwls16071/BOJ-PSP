# 스택 : 선입후출
# 큐 : 선입선출 => 큐 구현을 위해 deque 라이브러리 이용
# 재귀 함수 : 자기 자신을 다시 호출하는 함수, 재귀 함수의 종료 조건을 반드시 명시

# DFS알고리즘
def DFS(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = " ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

# graph의 원소를 이렇게 준 이유
# 0과 가까운것 (X), 1과 가까운것 (2, 3, 8), 2와 가까운것 (1, 7), 3과 가까운 것 (1, 4, 5)
# 4와 가까운것 (3, 5), 5와 가까운것 (3, 4), 6과 가까운것 (7), 7과 가까운것 (2, 6, 8), 8과 가까운것 (1, 7)
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9
DFS(graph, 1, visited)

# [step1] : 그래프를 준비합니다. (방문 기준: 번호가 낮은 인접 노드부터)
# - 시작 노드 : 1
# 시작 노드인 1을 스택에 삽입하고 방문 처리를 합니다.

# [step2] : 스택의 최상단 노드인 1에 방문하지 않은 2, 3, 8이 있습니다.
# 이 중에서 가장 작은 노드인 2를 스택에 넣고 방문 처리를 합니다.

# [step3] : 스택의 최상단 노드인 2에 방문하지 않은 인접 노드 7이 있습니다.
# 따라서 7번 노드를 스택에 넣고 방문 처리를 합니다.

# [step4] : 스택의 최상단 노드인 7에 방문하지 않은 인접 노드 6, 8이 있습니다.
# 이 중에서 가장 작은 노드인 2를 스택에 넣고 방문 처리를 합니다.

# [step5] : 스택의 최상단 노드인 6에 방문하지 않은 인접 노드가 없습니다.
# 따라서 스택에서 6번 노드를 꺼냅니다.

# [step6] : 스택의 최상단 노드인 7에 방문하지 않은 인접 노드는 8이 있습니다.
# 따라서 8번 노드를 스택에 넣고 방문 처리릏 합니다.

# BFS알고리즘(큐자료구조 =>선입선출, deque 라이브러리 사용)

from collections import deque

def BFS(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 떄까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9
BFS(graph, 1, visited)

# [step1] : 그래프를 준비합니다. (방문 기준: 번호가 낮은 인접 노드부터)
# - 시작 노드인 1을 큐에 삽입하고 방문 처리릏 합니다.

# [step2] : 큐에서 노드 1을 꺼내 방문하지 않은 인접 노드 2, 3, 8을 큐에 삽입하고 방문 처리합니다.

# [step3] : 큐에서 노드 2를 꺼내 방문하지 않은 인접 노드 7을 큐에 삽입하고 방문 처리합니다.

# [step4] : 큐에서 노드 3을 꺼내 방문하지 않은 인접 노드 4, 5를 큐에 삽입하고 방문 처리합니다.

# [step5] : 큐에서 노드 8을 꺼내고 방문하지 않은 인접 노드가 없으므로 무시합니다.

# [step6] : 큐에서 노드 7을 꺼내고 방문하지 않은 인접 노드인 6을 큐에 삽입하고 방문 처리를 합니다.

