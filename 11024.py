# 수 N개가 주어졌을 때, N개의 합을 구하는 프로그램을 작성하시오.

T = int(input())

for i in range(T):
    num_lst = list(map(int, input().split()))
    print(sum(num_lst))