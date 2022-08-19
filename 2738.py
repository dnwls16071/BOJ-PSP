# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

# 아래와 같은  2차원 배열의 구조
# 왼쪽 부분 코드는 배열 하나당 원소의 개수, 오른쪽 부분 코드는 반복 횟수

N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    temp = list(map(int, input().split()))

    for j in range(M):
        board[i][j] += temp[j]

for i in range(N):
    for j in range(M):
        print(board[i][j], end = " ")
    print()