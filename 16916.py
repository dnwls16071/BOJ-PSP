# 문자열 S의 부분 문자열이란, 문자열의 연속된 일부를 의미한다.

# 예를 들어, "aek", "joo", "ekj"는 "baekjoon"의 부분 문자열이고, "bak", "p", "oone"는 부분 문자열이 아니다.

# 문자열 S와 P가 주어졌을 때, P가 S의 부분 문자열인지 아닌지 알아보자.

S = input()
for _ in range(1):
    t = input()
    if t in S:
        res = 1
    else:
        res = 0
print(res)