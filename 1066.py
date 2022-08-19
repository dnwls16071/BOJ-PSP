# 체스판은 8×8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다. 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.

chess = []
for _ in range(0, 8):
    chess.append(list(map(str, input())))

answer = 0
for i in range(0, 8):
    for j in range(0, 8):
# if i % 2 == 0 and j % 2 == 0:은 성립이 안되는데 왜냐하면 i, j가 1인 경우가 들어가기 때문이다.        
# i, j 둘 다 짝수여야 가능하므로 어차피 짝수끼리의 합은 짝수이므로 아래와 같은 코드가 좋은 코드
        if (i + j) % 2 == 0:
            if chess[i][j] == "F":
                answer += 1
print(answer)