# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

import itertools

N, M = map(int, input().split())
number = list(map(int, input().split()))
number = sorted(number)

lst = list(itertools.combinations_with_replacement(number, M))
lst = list(set(lst))
lst.sort()

for i in lst:
    for j in i:
        print(j, end = " ")
    print()

# itertools의 중복조합을 사용한 문제였다.
# set()를 통해서 중복되는 요소를 제거하고 리스트로 바꾼 다음 오름차순 정렬하여 쉽게 풀 수 있었다.
