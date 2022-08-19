# 길이가 N인 수열 A1, A2, ..., AN이 주어진다. 이때, 다음 쿼리를 수행하는 프로그램을 작성하시오.

# i j k: Ai, Ai+1, ..., Aj로 이루어진 부분 수열 중에서 k보다 큰 원소의 개수를 출력한다.

N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())

res = 0
for _ in range(M):
    i, j, k = map(int, input().split())

    for a in range(i-1, j):
        if N_lst[a] > k:
            res += 1
    print(res)
    res = 0