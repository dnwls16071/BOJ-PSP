# 피제수(분자) A와 제수(분모) B가 있다. 두 수를 나누었을 때, 소숫점 아래 N번째 자리수를 구하려고 한다. 예를 들어, A=3, B=4, N=1이라면, A÷B=0.75 이므로 출력 값은 7이 된다.

A, B, N = map(int, input().split())

A %= B
for i in range(N-1):
    A = (A * 10) % B
print((A * 10) // B)

# 기본적으로 파이썬에서의 소수점 자릿수는 15자리까지 표시되는데 점점 길어질수록 인덱스에러가 출력될 수 있다.
# 수학적 원리를 정리하면 다음과 같다.

# for case1.
# 25 % 7 = 4 * 10 = 40
# 40 // 7 = 5(result)
#
# for case2.
# 40 % 7 = 5 * 10 = 50
# 50 // 7 = 7(result)
#
# for case3.
# 50 % 7 = 1 * 10 = 10
# 10 // 7 = 1(result)
#
# for case4.
# 10 % 7 = 3 * 10 = 30
# 30 // 7 = 4(result)

# for case5.
# 30 % 7 = 2 * 10 = 20
# 20 // 7 = 2(result)
# 정답: 2

# 위의 과정에서 보면 알 수 있듯이 나머지에 10을 곱하고 그 수를 다시 나눠주면 소수점 자릿수를 나타낼 수 있다.

