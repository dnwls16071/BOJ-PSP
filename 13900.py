# N개의 정수 중 서로 다른 위치의 두 수를 뽑는 모든 경우의 두 수의 곱의 합을 구하라.
#
# 예를 들어 N = 3이고 주어진 정수가 2, 3, 4일 때, 두 수를 뽑는 모든 경우는 (2, 3), (2, 4), (3, 4)이며 이때 각각의 곱은 6, 8, 12이다. 따라서 총합은 26이다.

# Code1
from itertools import combinations

N = int(input())
lst = list(map(int, input().split()))

result = []
for i in combinations(lst, 2):
    answer = 1
    for j in i:
        answer *= j
    result.append(answer)
print(sum(result))

# Code2
N = int(input())
lst = list(map(int, input().split()))

sum_nums = sum(lst)
result = 0

for i in lst:
    sum_nums -= i
    result += sum_nums * i
print(result)

# Code1의 방식처럼 from itertools import combinations(조합론)를 이용해서 풀려고 하면 시간 초과가 발생한다.
# 구글링해서 어떻게 순서쌍의 곱을 최소시간을 이용해서 풀 수 있을지 찾아보았다.

# 위의 알고리즘을 예시로 들어서 설명하면 다음과 같다.
# ex. (1 2 3 4 5) => (1 2)(1 3)(1 4)(1 5)(2 3)(2 4)(2 5)(3 4)(3 5)(4 5)

# 1 * (2 + 3 + 4 + 5) + 2 * (3 + 4 + 5) + 3 * (4 + 5) + 4 * 5
# 전체 합에서 앞의 수부터 하나씩 빼준 다음에 그 값을 곱해주면서 누적합 개념으로 생각하면 된다.
