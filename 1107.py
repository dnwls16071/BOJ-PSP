# 수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.
#
# 리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
#
# 수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
#
# 수빈이가 지금 보고 있는 채널은 100번이다.

import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
disabled_button = list(map(int, input().split()))
min_cnt = abs(100-N)    # 100번에서 N번으로 이동하기 위해서 눌러야 하는 최소 리모컨의 개수
if N == 100:
    print(0)
    exit(0)
else:
    for i in range(900001):
        i = str(i)
        for j in range(len(i)):
            if int(i[j]) in disabled_button:
                break
            elif j == len(i) - 1:
                min_cnt = min(min_cnt, abs(int(i)-N) + len(i))
print(min_cnt)

# 최대 채널의 번호는 500000번이다.
# 충분히 큰 수(900000 or 1000000)를 통해서 브루트포스(완전탐색)로 반복문을 돌렸다.
# 그리디 알고리즘보다는 브루트포스 알고리즘 스타일의 문제인 것 같다.

# 예제
# N = 500000
# M = 4
# 9 8 7 0

# 위의 예제인 경우 첫 번째, 466666번을 누르고 (+)버튼을 33334번 누르는 방법이 있다.
# 두 번째, 511111번을 누르고 (-)버튼을 11111번 누르는 방법이 있다.

# 첫 번째 누르는 리모컨 최소 버튼의 개수는 6 + 33334 = 33340번이다.
# 두 번째 누르는 리모컨 최소 버튼의 개수는 6 + 11111 = 11117번이다.