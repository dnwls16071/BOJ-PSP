# 수빈이가 세상에서 가장 좋아하는 것은 소수이고, 취미는 소수를 가지고 노는 것이다. 요즘 수빈이가 가장 관심있어 하는 소수는 7331이다.
#
# 7331은 소수인데, 신기하게도 733도 소수이고, 73도 소수이고, 7도 소수이다. 즉, 왼쪽부터 1자리, 2자리, 3자리, 4자리 수 모두 소수이다! 수빈이는 이런 숫자를 신기한 소수라고 이름 붙였다.
#
# 수빈이는 N자리의 숫자 중에서 어떤 수들이 신기한 소수인지 궁금해졌다. N이 주어졌을 때, 수빈이를 위해 N자리 신기한 소수를 모두 찾아보자.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)    # 재귀 깊이를 설정해준다.

def isPrime(number):    # 소수를 판별하는 함수
    number = int(number)
    for i in range(2, int(int(number)**0.5)+1):
        if number % i == 0:
            return False
    return True

def DFS(number):
    if len(number) == N:    # 만약 N자리 수 길이가 나오면?
        print(number)       # 해당 숫자 출력
        return
    for i in numbers:
        if isPrime(number + i): # 입력값에 i를 붙인 수가 소수를 반환하면?
            DFS(number + i)

N = int(input())
prime_number = ['2', '3', '5', '7']
numbers = ['1', '3', '7', '9']

for i in prime_number:
    DFS(i)

# 에라토스테네스의 체로 해당 구간을 전부 다 점검하려고 한다면 메모리 초과가 발생할 가능성이 높다.