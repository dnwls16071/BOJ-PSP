# 행복이는 길이가 $N$인 수열 $A$에서 소수들을 골라 최소공배수를 구해보려고 한다.
#
# 행복이를 도와 이를 계산해주자.

def isPrime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

N = int(input())
A = set(map(int, input().split()))

answer = 1
for i in A:
    if isPrime(i):
        answer *= i

if answer == 1:
    print(-1)
else:
    print(answer)

# 소수끼리는 서로 서로소 관계가 성립하므로 여러 개의 최소공배수를 구할때 따로 최대공약수, 최소공배수를 구하는 과정이 별도로 필요하지않다.
