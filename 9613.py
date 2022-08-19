# 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오

import math

T = int(input())

for i in range(T):
    num_lst = list(map(int, input().split()))
    total = 0
    for j in range(1, len(num_lst)):
        for k in range(j+1, len(num_lst)):  # j보다 1이 큰 위치의 수와 최대공약수를 계산해야하므로 범위를 이렇게 지정함
            total += math.gcd(num_lst[j], num_lst[k])
    print(total)