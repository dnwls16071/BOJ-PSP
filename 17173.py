# 신원이는 백준에서 배수에 관한 문제를 풀다가 감명을 받아 새로운 문제를 만들어보았다. 자연수 N과 M개의 자연수 Ki가 주어진다. Ki중 적어도 하나의 배수이면서 1 이상 N 이하인 수의 합을 구하여라.

N, M = map(int, input().split())
number = list(map(int, input().split()))

res = []
for i in range(1, N+1):
    for j in number:
        if i % j == 0:
            res.append(i)
res = set(res)
print(sum(res))