# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
#
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

import sys
input = sys.stdin.readline
A, B = map(int, input().split())

count = 1
while True:
    if A == B:
        break
    elif (B % 2 != 0 and B % 10 != 1) or (B < A):
        count = -1
        break
    else:
        if B % 10 == 1:
            B //= 10
            count += 1
        else:
            B //= 2
            count += 1
print(count)

# 그리디 알고리즘이 생각나서 바로 문제를 풀기 시작했다.
# 입력값으로부터 결과를 도출하는 방법은 복잡하고 시간도 오래 걸린다.
# 결과로부터 입력값을 도출하는 방법이 좋은 방법이 된다.

# 2를 곱한다. <=> 2를 나눈다.
# 1을 수의 가장 오른쪽에 추가한다. <=> 1이 수의 가장 오른쪽에 있으면 1을 제거한다.

