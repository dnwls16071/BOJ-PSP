# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

N, M = map(int, input().split())

a = set()
b = set()
for _ in range(N):
    a.add(input())

for _ in range(M):
    b.add(input())

result = list(a.intersection(b))
result.sort()

print(len(result))
for i in result:
    print(i)
