# 2차원 좌표 상의 여러 점의 좌표 (x,y)가 주어졌을 때, 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램을 작성하시오.

n = int(input()) #점의 개수를 출력

Q1_count = 0
Q2_count = 0
Q3_count = 0
Q4_count = 0
AXIS_count = 0

for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        AXIS_count += 1
    elif x > 0 and y > 0:
        Q1_count += 1
    elif x < 0 and y > 0:
        Q2_count += 1
    elif x < 0 and y < 0:
        Q3_count += 1
    elif x > 0 and y < 0:
        Q4_count += 1

print("Q1: {}".format(Q1_count))
print("Q2: {}".format(Q2_count))
print("Q3: {}".format(Q3_count))
print("Q4: {}".format(Q4_count))
print("AXIS: {}".format(AXIS_count))