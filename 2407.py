# nCm을 출력한다.

from math import factorial

n, m = map(int, input().split())
result = factorial(n) // (factorial(m) * factorial(n-m))
print(result)