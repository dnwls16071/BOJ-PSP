# 이번 ACM-ICPC 대회의 자리는 참가자들이 직접 정한다. 참가자들은 예비 소집일에 자신이 원하는 자리를 미리 정해놓았고, 대회 당일에 어제 적어놓은 자리에 앉으면 된다. 여러명이 같은 자리를 적어논 경우에는, 먼저 도착한 사람이 그 자리에 앉게되고, 앉지 못한 사람은 대회에 참가할 수 없다.

# 각 사람이 선호하는 자리가 주어졌을 때, 대회에 참가하지 못하는 사람의 수를 구하는 프로그램을 작성하시오.

K = int(input())

for i in range(K):
    P, M = map(int, input().split())
    seat = []

    for i in range(P):
        seat.append(int(input()))
    if M == 1:
        print(P-1)
    else:
        seat = set(seat)
        print(P-len(seat))
