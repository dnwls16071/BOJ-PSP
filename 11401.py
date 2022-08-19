# 자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수
# \(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())

if K > N - K:
    K = N - K

total = 1
for i in range(1, K+1):
    total = (total * N) // i
    N -= 1
print(total % 1000000007)