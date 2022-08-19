# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

# 1차 코드
N = int(input())
num_list = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in num_list:
    if i == v:
        cnt +=1
print(cnt)

# 2차 코드
N = int(input())
num_list = list(map(int, input().split()))
v = int(input())
print(num_list.count(v))