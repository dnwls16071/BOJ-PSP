# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

from itertools import combinations

N, S = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):
    comb = combinations(lst, i)
    
    for j in comb:
        if sum(j) == S:
            cnt += 1
print(cnt)