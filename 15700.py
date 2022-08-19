# N×M 크기의 벽에 2×1, 1×2 크기의 타일을 채우려고 한다. 겹치지 않게 놓는다면, 최대 몇 개를 채울 수 있을까?

N, M = map(int, input().split())

if N == 1:
    cnt = M // 2
elif M == 1:
    cnt = N // 2
else:
    cnt = (M * N) // 2
print(cnt) 
