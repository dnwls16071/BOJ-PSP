# 오늘도 서준이는 점근적 표기 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

# 알고리즘의 소요 시간을 나타내는 Θ-표기법(빅-쎄타)을 다음과 같이 정의한다.

# Θ(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 c1 × g(n) ≤ f(n) ≤ c2 × g(n)인 양의 상수 c1, c2, n0가 존재한다}

# 이 정의는 실제 Θ-표기법(https://en.wikipedia.org/wiki/Big_O_notation)과 다를 수 있다.

# 함수 f(n) = a1n + a0, 양의 정수 c1, c2, n0가 주어질 경우 Θ(n) 정의를 만족하는지 알아보자.

a1, a0 = map(int, input().split())
c1, c2 = map(int, input().split())
n0 = int(input())
lst = []
for n in range(n0, 101):
    if a1 * n + a0 >= c1 * n and a1 * n + a0 <= c2 * n:
        lst.append(1)
    else:
        lst.append(0)

if 0 in lst:
    print(0)
else:
    print(1)