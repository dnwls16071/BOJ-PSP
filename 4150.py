# 피보나치 수열은 다음과 같이 그 전 두 항의 합으로 계산되는 수열이다. 첫 두 항은 1로 정의된다.

# f(1) = 1, f(2) = 1, f(n > 2) = f(n − 1) + f(n − 2)

# 정수를 입력받아, 그에 해당하는 피보나치 수를 출력하는 프로그램을 작성하여라.

n = int(input())
fibonacci = [0, 1, 1]

for i in range(3, n+1):
    fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

print(fibonacci[n])
