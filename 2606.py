# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
#
# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.
#
# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

cnt = 0
def DFS(virus):
    global cnt
    # 현재 컴퓨터를 방문 처리
    visited[virus] = True

    for i in network[virus]:
        if not visited[i]:
            DFS(i)
            cnt += 1

N = int(input())
computer = int(input())
network = [[True] * (N+1) for _ in range(N+1)]

for i in range(computer):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = [False] * (N+1)
DFS(1)
print(cnt)

# DFS, BFS에서 배열 선언시에는 2차원 배열을 선언한다.
# DFS, BFS문제를 더 많이 접해봐야 감이 잡힐 것 같다.
