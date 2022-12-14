# 수학에서, 피보나치 수는 위의 점화식과 같이 귀납적으로 정의되는 수열이다. 위의 식에서도 알 수 있듯이, 피보나치 수 F(n)은 0 이상의 n에 대해서만 정의된다.
#
# 하지만 피보나치 수 F(n)을 n이 음수인 경우로도 확장시킬 수 있다. 위의 식에서 n > 1인 경우에만 성립하는 F(n) = F(n-1) + F(n-2)를 n ≤ 1일 때도 성립되도록 정의하는 것이다. 예를 들어 n = 1일 때 F(1) = F(0) + F(-1)이 성립되어야 하므로, F(-1)은 1이 되어야 한다.
#
# n이 주어졌을 때, 피보나치 수 F(n)을 구하는 프로그램을 작성하시오. n은 음수로 주어질 수도 있다.

n = int(input())
F = [0, 1]
for i in range(2, abs(n) + 1):
    F.append((F[i-2] + F[i-1]) % 1000000000)
if n % 2 == 0 and n < 0:    # n이 음수인데 짝수로 나뉘는 경우라면 -1을 출력
    print(-1)
elif n == 0:    # n이 0이면 0을 출력
    print(0)
else:   # n이 양수면 1을 출력
    print(1)
print(F[abs(n)])

# n = 1 => 1, n = -1 => 1
# n = 2 => 1, n = -2 => -1
# n = 3 => 2, n = -3 => 2
# n = 4 => 3, n = -4 => -3

# 피보나치 수열 확장 점화식에 값을 대입해서 정리해보면 n이 짝수이면 대칭 구조를 이룬다.
# n이 홀수이면 값이 똑같아진다.