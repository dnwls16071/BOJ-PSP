# 평면에 네 개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다. 이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭짓점이 겹칠 수도 있다.

# 이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.

# 2차원 배열의 작성
board = [[0 for _ in range(100)] for _ in range(100)]

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 1

count = 0
for a in board:
    count += sum(a)

print(count)