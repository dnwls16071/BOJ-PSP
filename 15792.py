# 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

import sys

A, B = map(int, sys.stdin.readline().split())

# print("{}".format(A/B))
print("%0.16f"%(A/B))