# 정우는 소문난 걸그룹 덕후이다. 정우의 친구 준석이도 걸그룹을 좋아하지만 이름을 잘 외우지 못한다는 문제가 있었다. 정우는 친구를 위해 걸그룹 개인과 팀의 이름을 검색하여 외우게 하는 퀴즈 프로그램을 만들고자 한다.

N, M = map(int, input().split())
group = {}

for _ in range(N):
    name = input()
    group[name] = []
    for _ in range(int(input())):
        group[name].append(input())
    group[name].sort()

for _ in range(M):
    quiz = input()
    if int(input()) == 1:
        for i in group[quiz]:
            print(M)
    else:
        for i in group.keys():
            if quiz in i:
                print(i)