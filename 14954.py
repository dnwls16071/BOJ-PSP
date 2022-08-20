# Consider the following function f defined for any natural number n:
#
# f(n) is the number obtained by summing up the squares of the digits of n in decimal (or base-ten).
#
# If n = 19, for example, then f(19) = 82 because 12 + 92 = 82.
#
# Repeatedly applying this function f, some natural numbers eventually become 1. Such numbers are called happy numbers. For example, 19 is a happy number, because repeatedly applying function f to 19 results in:
#
# f(19) = 12 + 92 = 82
# f(82) = 82 + 22 = 68
# f(68) = 62 + 82 = 100
# f(100) = 12 + 02 + 02 = 1
# However, not all natural numbers are happy. You could try 5 and you will see that 5 is not a happy number. If n is not a happy number, it has been proved by mathematicians that repeatedly applying function f to n reaches the following cycle:
#
# 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4.
#
# Write a program that decides if a given natural number n is a happy number or not.

def function(x):
    total = 0
    while x // 1 != 0:  # 0이 나오면 더 이상 진행할 수 없다.
        total += (x % 10) ** 2  # 각 자릿수의 제곱
        x = (x // 10)
    return total

N = int(input())
while True:
    N = function(N)
    if N == 4:
        print("UNHAPPY")
        break
    elif N == 1:
        print("HAPPY")
        break

# 영어로 된 코드문제였다. 문제를 해석해보면 다음과 같이 정리할 수 있다.
# f(n)은 n의 자릿수의 제곱을 10진수로 합산한 수이다.
# 모든 자연수가 HAPPY NUMBER는 아니다.
# 만약 n이 HAPPY NUMBER가 아니라면 f(n)을 반복적으로 수행했을때 다시 원래 n으로 귀결된다는 것이 수학자에 의해서 증명됨

# ex. 5 -> 25 -> 29 -> 85 -> 89 -> 145 -> 42 -> 20 -> 4
# ex. 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

