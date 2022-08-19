# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

import itertools

N, M = map(int, input().split())
number = list(map(int, input().split()))
number.sort()

lst = itertools.combinations(number, M)

for i in lst:
    print(*i)

# 조합론을 생각했는데 결과가 어떤거는 맞게 출력되고 어떤거는 맞게 출력되지않아서 많이 고민했던 문제였다.
# 그러던 중 문제에서 주어진 '오름차순'에 주목하게 되었고 리스트를 오름차순해주면 결과도 오름차순으로 출력되지않을까하는 생각이 들었다.
# 수학적 지식인 확률과 통계의 조합을 이용한 문제이며 백트래킹 알고리즘이 사용되는 문제였다.