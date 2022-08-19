# 10년 동안 도박판에서 야바위를 한 영훈은 이제 보지 않고도 구슬이 있는 컵을 맞추는 지경에 이르렀다.

# 이런 영훈을 골탕 먹이기 위해 문자열로 야바위를 하려고 한다.

# T번 동안 문자열 S의 A번째 위치에 있는 문자와 B번째 위치에 있는 문자를 바꾼 결과를 출력하는 프로그램을 작성하시오.

S = list(input())
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    S[A], S[B] = S[B], S[A]

print(''.join(S))