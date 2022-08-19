# N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

C = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):  # N = 3 (0, 1, 2)
    for k in range(K):  # K = 3 (0, 1, 2)
        for m in range(M):  # M = 2 (0, 1)
            C[n][k] += A[n][m] * B[m][k]

for i in C:
    for j in i:
        print(j, end = " ")
    print()

# 행렬에 대한 기본지식이 없어 문제를 이해하는데 시간이 많이 걸렸던 문제였다.
# 파이썬 행렬 곱셈은 N*M 행렬과 M*K 행렬이 만나 N*K행렬을 만든다.
