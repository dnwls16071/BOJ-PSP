# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

# 1차(시간초과)
# N = int(input())
# N_arr = sorted(map(int, input().split()))

# M = int(input())
# M_arr = list(map(int, input().split()))

# def binary_search(array, target, start, end):
#     if start > end:
#         return None
    
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] < target:
#         return binary_search(array, target, mid + 1, end)
#     else:
#         return binary_search(array, target, start, mid - 1)

# 2차   >   딕셔너리를 이용하는 방법도 공부할것
N = int(input())
N_lst = list(map(int, input().split()))

dict = {}
for i in N_lst:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
    
M = int(input())
M_lst = list(map(int, input().split()))

for i in M_lst:
    if i in dict:
        print(dict[i], end = " ")
    else:
        print(0, end = " ")