# 욱제는 15라는 수를 굉장히 싫어한다. 그래서 0으로 시작하지 않고 1과 5로만 구성된 $N$자리 양의 정수 중에서, 15의 배수가 몇 개인지 궁금해졌다.
#
# 참가자 여러분도 궁금하지요?
#
# 안 궁금함? 15ㄱ

N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1):
    if i % 2 == 0:
        dp[i] = (dp[i-1] * 2 + 1) % 1000000007
    else:
        dp[i] = (dp[i-1] * 2 - 1) % 1000000007
print(dp[N])