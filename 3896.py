# 양의 정수 N과, N보다 큰 소수 P가 주어질 때, N!을 P로 나눈 나머지를 구하여라.

from math import factorial

N, P = map(int, input().split())

tmp = factorial(N) % P
print(tmp)
