# 상근이는 덧셈과 나눗셈을 엄청나게 못한다. 이런 상근이를 위해 정인이는 상근이에게 다음과 같은 문제를 냈다.
#
# 정인이는 양의 정수 A,B,C,D로 이루어진 2*2 표를 그렸다.
#
# A	B
# C	D
# 위와 같은 표가 있을 때, 표의 값은 A/C + B/D 이다.
#
# 상근이는 표를 몇 번 돌리면 표의 값이 최대가 되는지 궁금해졌다.
#
# 표는 90도 시계방향으로 돌릴 수 있다.
#
# 문제 상단의 표를 1번 회전 시키면 다음과 같다.
#
# C	A
# D	B
# 2번 회전 시키면 다음과 같이 된다.
#
# D	C
# B	A
# 표에 쓰여 있는 A,B,C,D가 주어졌을 때, 표를 몇 번 회전시켜야 표의 값이 최대가 되는지 구하는 프로그램을 작성하시오.

A, B = map(int, input().split())
C, D = map(int, input().split())

rotation_value = []
rotation_value.append(A/C + B/D)  # 0번 회전한 값
rotation_value.append(C/D + A/B)  # 1번 회전한 값
rotation_value.append(D/B + C/A)  # 2번 회전한 값
rotation_value.append(B/A + D/C)  # 3번 회전한 값

max_value = max(rotation_value)
print(rotation_value.index(max_value))