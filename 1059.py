# 정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.
#
# A와 B는 양의 정수이고, A < B를 만족한다.
# A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
# 집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.

L = int(input())
lst = list(map(int, input().split()))
n = int(input())

lst.append(0)
lst.sort()

cnt = 0
for i in range(len(lst)-1):
    if lst[i] == n or lst[i+1] == n:
        cnt = 0
        break
    elif lst[i] < n and lst[i+1] > n:
        cnt = ((n - lst[i]) * (lst[i+1] - n)) - 1
        break
print(cnt)

# 좋은 구간의 개수를 어떻게 세줘야 할지 많이 고민했던 문제였다.
# (n - (n과 가장 가까운 리스트의 최솟값)) * ((n과 가장 가까운 리스트의 최댓값) - n) - 1