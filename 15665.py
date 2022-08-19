# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

from itertools import product

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = list(set(product(lst, repeat = M)))
result = sorted(result)

for i in result:
    print(*i)

# itertools 모듈 요점정리 4가지
# 1. commbinations : 조합 => combinations(lst, M)
# 2. combinations_with_replacement : 중복조합 => combinations_with_replacement(lst, M)
# 3. permutations : 순열 = > permutations(lst, M)
# 4. product : 중복순열 => product(lst, repeat = M)