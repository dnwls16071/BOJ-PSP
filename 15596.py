# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

def solve(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum
