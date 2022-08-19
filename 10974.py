# N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

if __name__ == "__main__":
    import itertools

    N = int(input())
    lst = [i for i in range(1, N+1)]    # 1부터 N까지 숫자들이 들어있는 리스트
    res = itertools.permutations(lst, N)
    for i in res:
        print(*i)

# itertools 라이브러리
# 순열 : from itertools import permutations
# permutations(iterable, r=None) : iterable에서 원소 개수가 r개인 순열 뽑기
# 이 때, r의 값을 지정해주지 않으면 최대 길이의 순열이 리턴된다.

# 조합 : from itertools import combinations
# combinations(iterable, r) : iterable에서 원소 개수가 r개인 조합 뽑기

# 중복조합 : from itertools import combinations_with_replacement
# combinations_with_replacement(iterable, r) : iterable에서 원소 개수가 r개인 중복 조합 뽑기
