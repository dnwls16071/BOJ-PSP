# 자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오

from math import factorial

N, K = map(int, input().split())

result = factorial(N) // (factorial(K) * factorial(N-K))

print(result % 10007)