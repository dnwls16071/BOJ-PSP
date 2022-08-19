# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# 1차 작성한 코드(시간 초과)
# N = int(input())
# N_lst = list(map(int, input().split()))

# M = int(input())
# M_lst = list(map(int, input().split()))

# for i in range(len(M_lst)):
#     if M_lst[i] in N_lst:
#         result = 1
#     else:
#         result = 0
#     print(result, end = " ")

# 2차 작성한 코드(이진 탐색)
import sys
input = sys.stdin.readline

N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))
N_lst.sort()

def binary_search(num):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if N_lst[mid] == num:
            return 1
        elif N_lst[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for num in M_lst:
    print(binary_search(num), end = " ") 