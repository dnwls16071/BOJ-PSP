# 버스 운전수 비와이 씨가 운전하는 버스(verse아님 ㅎ)는 N개의 정거장을 거친 후 종착역에 도착한다. 각 정거장은 내릴 인원수와 올라탈 인원수가 정해져 있다. 종착역에 도착하면 버스에 타고 있던 모든 사람이 내린다.

# 출발역과 종착역을 제외한 정거장의 수, 그리고 출발역에서 탑승하는 사람의 수
N, K = map(int, input().split())

for i in range(N):
    A, B = map(int, input().split())
print("비와이")