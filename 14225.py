# 수열 S가 주어졌을 때, 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성하시오.
#
# 예를 들어, S = [5, 1, 2]인 경우에 1, 2, 3(=1+2), 5, 6(=1+5), 7(=2+5), 8(=1+2+5)을 만들 수 있다. 하지만, 4는 만들 수 없기 때문에 정답은 4이다.

from itertools import combinations

N = int(input())
S = list(map(int, input().split()))

result = []
for i in range(1, N+1):
    lst = combinations(S, i)
    for val in lst:
        result.append(sum(val))
result.sort()
result = set(result)

standard_value = 1
while True:
    if standard_value in result:
        standard_value += 1
    else:
        break
print(standard_value)

# 조합을 이용한 방식으로 풀었고 합을 저장하는 과정에서 중복될수도 있으므로 집합 자료형으로 바꿨다.
# 누락된 자연수를 찾는것이므로 정렬하여 확인한후 해당하는 값이 없다면 break를 통해 탈출한다.