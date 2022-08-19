# 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.
# 배열에 정수 x (x ≠ 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

import sys
input = sys.stdin.readline

import heapq
N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if len(heap) != 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

# 이번 문제는 heapq에 관련된 문제로 좀 생소해서 구글링을 많이 하면서 이것저것 공부를 많이 했던 문제였다.
# 힙 리스트에 저장할 때 튜플형태로 (절댓값, 입력값)으로 저장하여 절대값을 기준으로 정렬할 수 있도록 한다

# 이 힙에서 가장 작은 원소를 출력하라고했는데 그렇다면 정렬을 오름차순으로 해줘야하는데... 어떻게 코드를 써야할지 몰랐다.
# heapq 모듈에 있는 함수 중에서 heapq.heappop(heap)를 활용했다.
# heapq.heappop(heap)는 heap에서 '가장 작은 원소'를 pop & 리턴하는 함수이다.

# heapq 모듈에 있는 함수 중에서 heapq.heappush(heap, x)를 활용했다.
# 이 때 원소를 집어넣으면 자동으로 오름차순으로 정렬을 하게 된다.

# 힙에 대한 내은 깃허브 문법 정리에 남겨놓았으니 참고하도록 하자.