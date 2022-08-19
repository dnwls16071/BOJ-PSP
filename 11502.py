# 정수론(수학)에서, 세 개의 소수 문제(3-primes problem) 는 다음과 같은 추측을 말한다.
#
# '5보다 큰 임의의 홀수는 정확히 세 개의 소수들의 합으로 나타낼 수 있다. 물론 하나의 소수를 여러 번 더할 수도 있다.'
#
# 예를 들면,
#
# 7 = 2 + 2 + 3
# 11 = 2 + 2 + 7
# 25 = 7 + 7 + 11
# 5보다 큰 임의의 홀수를 입력받아서, 그 홀수가 어떻게 세 소수의 합으로 표현될 수 있는지 (또는 불가능한지) 알아보는 프로그램을 작성하시오.

from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    prime_number = int(input())
    lst = combinations_with_replacement(range(1, prime_number + 1), 3)
    result = []
    for i in lst:
        if sum(i) == prime_number:
            result.append(i)
    while True:
        j = 0
        k = 0
        if result[j][k] == 1:
            result.remove(result[j])
        else:
            break

    if result == []:
        print(0)
    else:
        print(result[0])

# 중복조합을 이용해서 코드를 작성해봤는데 시간초과가 나와서 어디가 문제인지 많이 고민했던 문제였다.

def check_sum(lst, s):
    for a in lst:
        for b in lst:
            for c in lst:
                if a + b + c == s:
                    print(a, b, c)
                    return
    print(0)


def findPrime(num):
    data = list(range(2, num + 1))
    result = []

    while len(data) != 0:
        m = data[0]
        result.append(m)
        cnt = 0
        while cnt < len(data):
            if data[cnt] % m == 0:
                data.pop(cnt)
                cnt -= 1
            cnt += 1
    return result

T = int(input())
lst = []
for _ in range(T):
    lst.append(int(input()))
for i in lst:
    check_sum(findPrime(i), i)

# 구글링해서 다른 코드를 참고해서 이해하려고 해봤다.
