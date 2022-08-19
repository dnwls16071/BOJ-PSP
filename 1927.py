# 널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# heap 정렬 , heapq 패키지
import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    command = int(input())
    if command == 0:    # 만약 command가 0이라면?
        if not heap:    # 만약 heap안에 원소가 아무것도 없다면?
            print(0)    # 0을 출력
        else:           # 만약 heap 안에 원소가 있었다면?
            print(heapq.heappop(heap))  # heap안에서 가장 작은 원소값을 출력
    else:               # 만약 command가 0이 아닌 다른 값이라면?
        heapq.heappush(heap, command)   # heap에 원소 추가