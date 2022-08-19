# 음 아닌 정수 N이 주어졌을 때, 이 수를 서로 다른 정수 M(M ≥ 1)개의 팩토리얼의 합으로 나타낼 수 있는지 알아내는 프로그램을 작성하시오. 예를 들어 2=0!+1!로 나타낼 수 있지만, 5는 이와 같은 방식으로 나타낼 수 없다.

# 시간초과가 나온 이유를 생각해보자.
# 0부터 순차적으로 증가시킨 방법을 사용한 1차 코드
# 정말 큰 값에서 빼준다고 반대로 생각해보자.(2차코드)

# 1차 작성코드(시간 초과)
# import sys
# from math import factorial
# input = sys.stdin.readline

# N = int(input())    
# res = factorial(N)  # N의 팩토리얼 값

# num = 0
# tmp = 0
# while True:
#     tmp += factorial(num)
#     if res > tmp:
#         num += 1
#     elif res < tmp:
#         break
#     elif res == tmp:
#         print("YES")
# print("NO")

# 2차 코드
import sys
input = sys.stdin.readline

N = int(input())
if N == 0:
    N = -1
res = 2435902008176640000   # 20!의 값
for i in range(20, 0, -1):
    res = int(res // i)
    if N >= res:
        N = N - res

if N == 0:
    print("YES")
else:
    print("NO")