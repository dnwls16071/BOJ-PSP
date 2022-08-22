# 상근이는 학생들에게 두 양의 정수 A와 B의 최대공약수를 계산하는 문제를 내주었다. 그런데, 상근이는 학생들을 골탕먹이기 위해 매우 큰 A와 B를 주었다.
#
# 상근이는 N개의 수와 M개의 수를 주었고, N개의 수를 모두 곱하면 A, M개의 수를 모두 곱하면 B가 된다.
#
# 이 수가 주어졌을 때, 최대공약수를 구하는 프로그램을 작성하시오.

def gcd(a, b):
    while b != 0:
        remain = a % b
        a = b
        b = remain
    return str(a)

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

a = 1
for i in A:
    a *= i

b = 1
for i in B:
    b *= i

if len(gcd(a, b)) > 9:
    print(a[-1:-10])
else:
    print(int(gcd(a,b)))

# 골드5 난이도치곤 많이 쉬웠던 문제였다.
# 유클리드 호제법을 이용해서 최대공약수를 구해주었고 그 최대공약수를 문자화시켜 반환했다.
# 반환한 최대공약수의 자릿수가 9자리를 넘으면 마지막 9자리를 출력하고, 아니라면 정수화시켜 출력했다.
