# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

# code1
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))

sum_lst = [0]
total = 0
for i in range(len(lst)):
    total += lst[i]
    sum_lst.append(total)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_lst[j] - sum_lst[i-1])

# 구간별 누적합을 담은 리스트를 만들어 계산의 이중성을 최소화하여 수행 시간이 짧게 걸리게끔 작성했다.

# code2
N, M = map(int, input().split())
lst = list(map(int, input().split()))
for _ in range(M):
    i, j = map(int, input().split())
    print(sum(lst[:j]) - sum(lst[:i-1]))

# 이 방법이 왜 시간 초과가 나왔는지 알 것 같았다.
# 리스트가 길고 범위가 넓은 경우 처음부터 일일이 넣어서 합을 계산하는것은 많은 시간이 걸린다고 생각되었다.

# code 3
from itertools import accumulate

N, M = map(int, input().split())
lst = list(map(int, input().split()))
sum_lst = list(accumulate(lst))
sum_lst.insert(0, 0)
for _ in range(M):
    i, j = map(int, input().split())
    print(sum_lst[j] - sum_lst[i-1])

# from itertools import accumulate(누적합 모듈)을 사용해서도 가능할 것 같았다.
# Python3에서는 시간 초과가 발생했지만 PyPy3에서는 정상적으로 동작되었다.