# $n \choose m$의 끝자리 $0$의 개수를 출력하는 프로그램을 작성하시오.

N, M = map(int, input().split())

def two_count(number):
    two_cnt = 0
    while number != 0:
        number //= 2
        two_cnt += number
    return two_cnt

def five_count(number):
    five_cnt = 0
    while number != 0:
        number //= 5
        five_cnt += number
    return five_cnt

two_value = two_count(N) - two_count(N-M) - two_count(M)
five_value = five_count(N) - five_count(N-M) - five_count(M)
print(min(two_value, five_value))

# 끝자리가 0이라는 것은 2와 5의 곱으로 이루어져있다는 것을 의미한다.
# ex. xxxxx00 이면 2, 5가 각각 2개의 곱으로 이루어져있다.
# 따라서 위와 같이 2와 5의 개수를 구해주면된다.
# 2, 5가 같이 한 쌍이 존재해야 0이 생기므로 두 수의 횟수 중에서 최소값을 구하면 된다.
