# 중간고사를 시원하게 망친 찬우는 오늘부터 1분도 쉬지 않고 기말고사 공부에 매진하기로 다짐했다.
#
# 기말고사는 정확히 $24\times N$시간 이후에 시작되며, 쉬는 시간 없이 하루에 모든 과목의 시험을 보기 때문에 찬우는 $24\times N$시간동안 공부할 수 있다. 기말고사를 보는 과목은 총 $M$개로, 시험 시간이 빠른 과목부터 각각 $1$부터 $M$까지의 번호가 매겨져 있다. 모든 과목의 최저점은 $0$점, 최고점은 $100$점이다.
#
# 찬우는 공부를 하나도 하지 않아도 $i$번 과목에서 $a_{i}$ 점을 받을 수 있으며, $i$번 과목을 정확히 한 시간 공부할 때마다 그 과목의 성적을 $b_{i}$점 올릴 수 있다. 하지만 $i$번 과목을 30분 공부한다고
#
# $\frac{b_{i}}{2}$점이 오르지는 않으며, 아무리 공부하더라도 한 과목에서 최고점인 $100$점이 넘는 점수를 받을 수는 없다.
#
# 모든 과목의 점수의 합이 찬우의 최종 성적이 된다. 높은 성적을 받기 위한 최적의 전략으로 공부할 때, 찬우가 받을 수 있는 최종 성적의 최댓값을 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

# 만약 최댓값을 가지는 박스가 크레인이 감당할 수 있는 최대 중량보다 크다면?
if max(B) > max(A):
    print(-1)
    sys.exit(0)
else:
    time = 0
    while B:
        if not B:
            break
        for a in A:
            for b in B:
                if a >= b:
                    B.remove(b)
                    break
        time += 1
print(time)

# Python3로는 시간초과가 나왔지만 PyPy3로는 정답이 되었다.
