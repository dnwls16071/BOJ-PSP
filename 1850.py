# 모든 자리가 1로만 이루어져있는 두 자연수 A와 B가 주어진다. 이때, A와 B의 최대 공약수를 구하는 프로그램을 작성하시오.
#
# 예를 들어, A가 111이고, B가 1111인 경우에 A와 B의 최대공약수는 1이고, A가 111이고, B가 111111인 경우에는 최대공약수가 111이다.

# A, B = map(int, input().split())
#
# def GCD(a, b):
#     while b != 0:
#         remain = a % b
#         a = b
#         b = remain
#     return a
#
# tmp1 = int(str(1) * A)
# tmp2 = int(str(1) * B)
#
# print(GCD(tmp1, tmp2))

# 유클리드 호제법을 이용해 최대공약수를 구하는 함수를 작성했다.
# 하지만 메모리 초과라는 결과가 떠서 어디가 문제인지 알 수가 없었다.

A, B = map(int, input().split())

def GCD(a, b):
    while b != 0:
        remain = a % b
        a = b
        b = remain
    return a

print('1' * GCD(A, B))

# 그런데 1을 최대공약수만큼 반복해주면 정답이 된다.
