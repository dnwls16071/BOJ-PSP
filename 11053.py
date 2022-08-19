# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 일반적인 방법
N = int(input())
lst = list(map(int, input().split()))

res = 1
for i in range(len(lst)-1):
    if lst[i] < lst[i+1]:
        res += 1
print(res)

# 다이나믹 프로그래밍 이용 방법
N = int(input())
lst = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))