# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = list(set(combinations(lst, M)))
result = sorted(result)

for i in result:
    print(*i)