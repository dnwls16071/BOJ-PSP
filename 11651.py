# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 1차 작성 코드
import sys

N = int(sys.stdin.readline())

num_lst = []
for i in range(N):
    num_lst.append(list(map(int, sys.stdin.readline().split())))

num_lst.sort(key = lambda num : (num[1], num[0]))

for i in num_lst:
    print(i)

# 2차 작성 코드
import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key=lambda x: (x[1], x[0]))
for i in so:
    print(i[0], i[1])