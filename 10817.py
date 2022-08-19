# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

#1번 코드
A, B, C = map(int, input().split())

if A > B and A > C:
    if B > C:
        print(B)
    else:
        print(C)
if B > A and B > C:
    if A > C:
        print(A)
    else:
        print(C)
if C > A and C > B:
    if A > B:
        print(A)
    else:
        print(B)

#2번 코드
num_list = list(map(int, input().split()))
num_list.sort()
print(num_list[1])


