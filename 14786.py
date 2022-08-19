# A, B, C가 주어졌을 때, Ax+Bsin(x)=C를 만족하는 x를 찾는 프로그램을 작성하시오.

from math import sin

A, B, C = map(int, input().split())
x = 0

if A*x + B*sin(x) == C:
    print(x)