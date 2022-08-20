# 음 아닌 정수 N이 주어졌을 때, 이 수를 서로 다른 정수 M(M ≥ 1)개의 팩토리얼의 합으로 나타낼 수 있는지 알아내는 프로그램을 작성하시오. 예를 들어 2=0!+1!로 나타낼 수 있지만, 5는 이와 같은 방식으로 나타낼 수 없다.

import sys
n = int(sys.stdin.readline().rstrip())

res = 2432902008176640000   # 20!
if n == 0:
    n -= 1
for i in range(20, 0, -1):
    res = res//i
    if n >= res:
        n -= res

if n == 0:
    print("YES")
else:
    print("NO")

# 20!의 값은 1,000,000,000,000,000,000보다 큰 최초의 값이 된다.