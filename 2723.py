# 연종이는 창업했다. 오늘은 창업한지 N일이 되었고, 매일 매일 수익을 적어놓았다.

# 어느 날 연종이는 가장 많이 돈을 번 구간이 언제인지 궁금해졌다.

# 오늘이 창업한지 6일 되었고, 수익이 다음과 같다고 하자.

# 1일: -3
# 2일: 4
# 3일: 9
# 4일: -2
# 5일: -5
# 6일: 8
# 이때, 가장 많은 돈을 번 구간은 2~6까지이고 총 수입은 14이다.

import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break
    lst = [int(input()) for _ in range(N)]
    for i in range(1, N):
        lst[i] = max(lst[i], lst[i] + lst[i-1])
    print(max(lst))
    
# 다이나믹 프로그래밍
# lst[0] = -3원
# lst[1] = lst[0] + lst[1] > 1원
# lst[2] = lst[1] + lst[2] > 10원
# lst[3] = lst[3] + lst[2] > 8원
# lst[4] = lst[4] + lst[3] > 6원
# lst[5] = lst[5] + lst[4] > 14원
# i일을 기준으로 보았을때, i-1일까지의 합과 i일을 더해서 새로 갱신해준다.