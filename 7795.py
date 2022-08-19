# 심해에는 두 종류의 생명체 A와 B가 존재한다. A는 B를 먹는다. A는 자기보다 크기가 작은 먹이만 먹을 수 있다. 예를 들어, A의 크기가 {8, 1, 7, 3, 1}이고, B의 크기가 {3, 6, 1}인 경우에 A가 B를 먹을 수 있는 쌍의 개수는 7가지가 있다. 8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1.

# 두 생명체 A와 B의 크기가 주어졌을 때, A의 크기가 B보다 큰 쌍이 몇 개나 있는지 구하는 프로그램을 작성하시오.

# 1차 작성한 코드(시간초과)
# import sys

# T = int(sys.stdin.readline())
# for i in range(T):
#     N, M = map(int, sys.stdin.readline().split())
#     A = list(map(int, sys.stdin.readline().split()))
#     B = list(map(int, sys.stdin.readline().split()))
#     A.sort(reverse=True)
#     B.sort(reverse=True)
    
#     count = 0
#     for j in range(len(A)):
#         for k in range(len(B)):
#             if A[j] > B[k]:
#                 count += 1
#     print(count)

# 2차 작성한 코드(이진탐색 bisect를 활용)
from bisect import bisect_left, bisect_right

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    count = 0
    for a in A:
        count += bisect_left(B, a) 

    print(count)