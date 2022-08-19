# 수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.

# 다이나믹 프로그래밍을 이용한 방법
N = int(input())
lst = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if lst[i] < lst[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))