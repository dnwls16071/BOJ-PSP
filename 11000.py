# 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

# 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

# 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

# 수강신청 대충한 게 찔리면, 선생님을 도와드리자!

# 클래스 리스트에 원소를 넣을 때 튜플로 받아오는 방식
N = int(input())
Class = []
for _ in range(N):
    S, T = map(int, input().split())
    Class.append((S, T))
Class.sort(lambda x: (x[1], x[0]))

end_time = 0
cnt = 0
for S, T in Class:
    if S >= end_time:
        end_time = T
        cnt += 1
print(cnt)

# 클래스 리스트에 원소를 넣을 때 리스트로 받아오는 방식
import sys
import heapq
input = sys.stdin.readline
N = int(input())

lst = []
for _ in range(N):
    S, T = map(int, input().split())
    lst.append([S, T])
lst.sort()

room = []
heapq.heappush(room, lst[0][1])
for i in range(1, N):
    if lst[i][0] < room[0]:
        heapq.heappush(room, lst[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lst[i][1])
print(len(room))