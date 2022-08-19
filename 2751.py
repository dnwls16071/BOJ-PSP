# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 1차 작성한 코드(시간 초과)
# import sys
# input = sys.stdin.readline()

# N = int(sys.stdin.readline())

# num_list = []
# for _ in range(N):
#     num_list.append(int(sys.stdin.readline()))
# num_list.sort()

# for i in num_list:
#     print(i) 

# # 2차 작성한 코드
# n=int(input())
# num=[]

# for _ in range(n):
#     x = int(input())
#     num.append(x)

# for i in sorted(num):
#     print(i)

# 3차 작성한 코드
N = int(input())

num = [0] * 1000000

for _ in range(N):
    temp = int(input())
    if num[temp] == 0:
        num[temp] += 1

for i in range(0, 1000000):
    if num[i] == 1:
        print(i)


# 참고 답안 코드
# import sys
# m = int(input())

# for _ in range(m):
#     a = list(map(int, sys.stdin.readline()))
#     a.sort()
# for i in a:
#     print(i)