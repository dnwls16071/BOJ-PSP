# 지금까지 안 나온 별 찍기가 뭐가 있는지 생각해본 후, 별을 적절히 찍으세요.

N = int(input())

if N == 1:
    print("*")
elif N >= 2:
    for i in range(N):
        print("*"*N)