# 몇 개의 자연수로 이루어진 두 집합 A와 B가 있다. 집합 A에는 속하면서 집합 B에는 속하지 않는 모든 원소를 구하는 프로그램을 작성하시오.

A, B = map(int, input().split())
A_element = set(map(int, input().split()))
B_element = set(map(int, input().split()))

res = A_element.difference(B_element)
res = list(res)
res.sort()

print(len(res))
for i in res:
    print(i, end = " ")