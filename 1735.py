# 분수 A/B는 분자가 A, 분모가 B인 분수를 의미한다. A와 B는 모두 자연수라고 하자.
#
# 두 분수의 합 또한 분수로 표현할 수 있다. 두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하는 프로그램을 작성하시오. 기약분수란 더 이상 약분되지 않는 분수를 의미한다.

first_a, first_b = map(int, input().split())
second_a, second_b = map(int, input().split())

# 분모를 통분했을때 분자값을 더한 결과
tmp = first_a * second_b + second_a * first_b

def GCD(a,b):
    while b != 0:
        remain = a % b
        a = b
        b = remain
    return a

N = GCD(tmp, first_b * second_b)
print(tmp // N, (first_b * second_b) // N)

# 잘못 작성한 코드
first_a, first_b = map(int, input().split())
second_a, second_b = map(int, input().split())

# 분모를 통분했을때 분자값을 더한 결과
tmp = first_a * second_b + second_a * first_b
print(tmp, first_b * second_b)

# 이 방법이 답이 될 수 없는 이유
# 분자, 분모가 서로 기약분수가 될 수 없는 형태가 나올 수도 있기 때문에