# n개의 자연수로 이루어진 수열이 주어질 때, 특정 구간 [i,j](i≤j)의 합이 k보다 큰 모든 쌍 i,j의 개수를 출력하시오.

import sys
input = sys.stdin.realdine
n = int(input())
lst = list(map(int, input().split()))
k = int(input())

num = []
tmp = 0
cnt = 0
for i in lst:
    tmp += i
    num.append(tmp)

for i in range(n-1, -1, -1):
    j = 0
    if num[i] > k:
        cnt += 1
    while num[i] - num[j] > k:
        cnt += 1
        j += 1
print(cnt)

# 보편적인 투포인터 문제와는 좀 다른 문제였다.
# 리스트의 길이가 길어지면 원하는 구간의 구간합을 계산하는데 매우 오랜 시간이 걸릴 수 있다.
# 그 문제를 해결하기위해서 반복문으로 누적합을 구해서 새로운 리스트를 만들어준다.
# num = [1, 3, 6, 8, 9]
# num[4] - num[0] => 구간 [0:5]의 합에서 구간 [0:1]의 합을 빼준 결과와 동일한 의미(구간 [1:5]의 구간합)
# num[4] - num[1] => 구간 [0:5]의 합에서 구간 [0:2]의 합을 빼준 결과와 동일한 의미(구간 [2:5]의 구간합)
# Python3에서는 시간 초과가 나왔다.

# ex. 1 2 3 2 1 => num = [1, 3, 6, 8, 9]를 리스트에 넣어준다.
# j = 0 => num[5] - num[0] = 8 > 구간 [1:5]까지의 누적합
# j = 1 => num[5] - num[1] = 6 > 구간 [2:5]까지의 누적합
# 이런 식으로 코드를 작성하면 된다.
