# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# N개의 자연수 중에서 M개를 고른 수열

from itertools import permutations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = list(set(permutations(lst, M)))
result = sorted(result)

for i in result:
    print(*i)

# 조합과 순열은 명백히 다른 개념이다.
# 조합은 순서를 고려하지않지만 순열은 순서를 고려하므로 셀 수 있는 수가 차이가 난다.