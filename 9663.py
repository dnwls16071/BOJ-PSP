# N개의 퀸을 서로 적절히 배치하여 공격할 수 없는 경우의 수를 구하는 문제

def check(x):
    for i in range(x):
        # 다음과 같은 조건문을 써주는 이유
        # 우선 퀸이 서로 공격할 수 없도록 배치하는 경우를 생각해보면 다음과 같다.
        # 첫째, 서로 다른 퀸은 같은 행/열에 배치될 수 없다.
        # 둘째, 서로 다른 퀸은 같은 대각선 상에 배치될 수 없다.
        if chess[x] == chess[i] or abs(chess[i]-chess[x]) == x-i:
        # 행/열의 값이 같은 경우(chess[x] == chess[i])
        # 대각선의 값이 같은 경우(chess[i] - chess[x]) == x - i
            return False
    return True

def queen(x):
    global res
    if x == N:
        res += 1
        return
    for i in range(N):
        chess[x] = i
        if check(x):
            queen(x+1)

N = int(input())
res = 0
# 체스판을 2차원 배열로도 생각해도되지만 1차원 배열로도 생각할 수 있다.
# chess[1][2] = 5 => chess[1] = 2 (1행 2열)
chess = [0] * N
queen(0)
print(res)

# 머리로는 이해가 됐지만 이걸 코딩으로 구현하려니까 많이 어려웠던 문제였다.
