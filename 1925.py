# 평면상에 세 개의 점이 주어지면, 그 세 점으로 이루어지는 삼각형은 유일하게 결정된다. 또는, 삼각형이 이루어지지 않기도 한다. 세 점의 좌표가 주어졌을 때 다음에 따라 이 삼각형의 종류를 판단하는 프로그램을 작성하시오.

# 세 점이 일직선 위에 있으면 - ‘삼각형이 아님’  출력할 때는 X
# 세 변의 길이가 같으면 - ‘정삼각형’ 출력할 때는 JungTriangle
# 두 변의 길이가 같으면
# 가장 큰 각이 90°보다 크면 - ‘둔각이등변삼각형’ 출력할 때는 Dunkak2Triangle
# 가장 큰 각이 90°이면 - ‘직각이등변삼각형’ 출력할 때는 Jikkak2Triangle
# 가장 큰 각이 90°보다 작으면 - ‘예각이등변삼각형’ 출력할 때는 Yeahkak2Triangle
# 세 변의 길이가 모두 다르면
# 가장 큰 각이 90°보다 크면 - ‘둔각삼각형’ 출혁할 때는 DunkakTriangle
# 가장 큰 각이 90°이면 - ‘직각삼각형’ 출력할 때는 JikkakTriangle
# 가장 큰 각이 90°보다 작으면 - ‘예각삼각형’ 출력할 때는 YeahkakTriangle

import math

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
a = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
b = math.sqrt((x2 - x3)**2 + (y2 - y3)**2) 
c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2) 
a
# 일직선 상 위에 세 점이 있으므로 '삼각형이 아님'
if x1 == x2 == x3 == 0 or y1 == y2 == y3 == 0:
    print("X")
# 세 변의 길이가 같으면 '정삼각형'
elif a == b == c:
    print("JungTriangle")
# 두 변의 길이가 같으면?
elif a == b:
    if 
elif a == c:

elif b == c:
# 세 변의 길이가 모두 다르면?
elif a != b != c:
    