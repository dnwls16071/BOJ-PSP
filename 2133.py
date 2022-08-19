# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

N = int(input())
dp = [0] * 31
dp[2] = 3
dp[4] = 11

for i in range(6, 31, 2):
    dp[i] = (dp[2] * dp[i-2]) + (dp[i-2] - dp[i-4])
print(dp[N])

# 말로는 설명하기 너무 힘들어서 그림으로 노가다 뛰었다.
# 몇 개의 항을 구하고보니 규칙이 눈에 보였다.
# 일단 N이 홀수인 경우는 성립될 수 없다. 왜냐하면 겹쳐서 조건에 부합하지 않기 때문이다.
# dp[2] = 3, dp[2] = 11, dp[6] = 41, dp[8] = 153... 이 나온다.