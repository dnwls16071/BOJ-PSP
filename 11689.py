# 자연수 n이 주어졌을 때, GCD(n, k) = 1을 만족하는 자연수 1 ≤ k ≤ n 의 개수를 구하는 프로그램을 작성하시오.

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())

    def gcd(a, b):
        while b != 0:
            remain = a % b
            a = b
            b = remain
        return a

    cnt = 0
    for k in range(1, n+1):
        if gcd(n, k) == 1:
            cnt += 1
    print(cnt)

# 문제를 보고 최대공약수가 1인 수들의 개수를 구하는 것이라 생각해서 유클리드 호제법을 이용해서 코드를 작성했다.
# 하지만 시간초과가 나와서 당황스러웠던 문제였다.
# 문제를 다시 한 번 해석하면 다음과 같다.
# GCD(n, k) = 1 => 자연수 n과 k가 서로소 관계에 있다.

n = int(input())
result = n
for i in range(2, int(n**0.5)+1):
    if n % i == 0:  # 만약 n이 i로 나뉜다면?
        while n % i == 0:
            n //= i
        result = result * (1 - (1 / i))
if n > 1:   # n이 i로 안 나눠진 상태 + 만약 n이 1보다 크다면?
    result = result * (1 - (1 / n)) # 오일러 피 함수롤 사용
print(round(result))

# 오일러 피 함수 간략히 설명 => GCD(n, k)
# n * (1 - 1 / p1) * (1 - 1 / p2) ... 이 때, p1, p2..는 소인수
# 유클리드 호제법, 오일러 피 함수 사용