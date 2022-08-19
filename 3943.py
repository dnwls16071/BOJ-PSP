# 헤일스톤 수열은 다음과 같이 정의 한다.

# n이 짝수라면, 2로 나눈다.
# n이 홀수라면, 3을 곱한 뒤 1을 더한다.
# 헤일스톤 추측은 임의의 양의 정수 n으로 수열을 시작한다면, 항상 4, 2, 1, 4, 2, 1,...로 끝난다는 추측이다. 이 문제에서는 1이 나오면 수열이 끝난 것으로 처리한다.

# n이 주어졌을 때, 이 수열에서 가장 큰 값을 찾아 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    lst = []    # 헤일스톤 수열
    n = int(input())
    while True:
        if 1 in lst:
            break
        lst.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(max(lst))

# 입력값으로 1을 받는 경우 초기엔 빈 리스트가 없어 max값을 구할 수 없다.
# 따라서 위와 같이 코드를 작성하면 된다.