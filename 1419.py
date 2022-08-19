# 1부터 N까지의 수를 임의로 배열한 순열은 총 N! = N×(N-1)×…×2×1 가지가 있다.
#
# 임의의 순열은 정렬을 할 수 있다. 예를 들어  N=3인 경우 {1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2}, {3, 2, 1}의 순서로 생각할 수 있다. 첫 번째 수가 작은 것이 순서상에서 앞서며, 첫 번째 수가 같으면 두 번째 수가 작은 것이, 두 번째 수도 같으면 세 번째 수가 작은 것이….
#
# N이 주어지면, 아래의 두 소문제 중에 하나를 풀어야 한다. k가 주어지면 k번째 순열을 구하고, 임의의 순열이 주어지면 이 순열이 몇 번째 순열인지를 출력하는 프로그램을 작성하시오.

from itertools import permutations

N = int(input())
L = list(permutations(range(1, N+1), 4))
lst = list(map(int, input().split()))

if len(lst) == 2:   # 소문제 번호가 1인 경우 => 순열 출력
    print(*L[lst[1]])
else:   # 소문제 번호가 2인 경우 => 순서 출력
    l = list(lst[1:])
    result = ' '.join(s for s in l)
    for i in range(len(L)):
        tmp = ' '.join(t for t in L[i])
