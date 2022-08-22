# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = []
tmp = []
for _ in range(N):
    command = int(input())
    if command == 0:
        if not heap:    # 배열이 비어있으면?
            print(0)
        else:   # 배열이 비어있지않으면?
            tmp.append(heapq.heappop(heap))
            print(-heapq.heappop(tmp))
    else:
        heapq.heappush(heap, -command)

# 참고 문제 : 1927번(최소 힙)

# 최대 힙을 구현할때는 (-)를 넣어줘야 한다는 것을 꼭 명심하자.