# 자연수 N이 주어졌을 때, 2의 제곱수면 1을 아니면 0을 출력하는 프로그램을 작성하시오.

# 1차 작성한 코드(시간 초과)
# N = int(input())
# num = [pow(2, i) for i in range(0, N+1)]

# if N in num:
#     print(1)
# else:
#     print(0)

# 2차 작성한 코드
N = int(input())
num = [2**i for i in range(31)]

if N in num:
    print(1)
else:
    print(0)