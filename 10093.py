# 두 양의 정수가 주어졌을 때, 두 수 사이에 있는 정수를 모두 출력하는 프로그램을 작성하시오.

# 쉬운 문제라고 생각했지만 두 수 사이에 수가 존재하지않는 경우를 뒤늦게 생각하여 시간이 좀 걸렸던 문제
A, B = map(int, input().split())

if A != B:
    if A > B:
        A, B = B, A
        print(B-A-1)
        for i in range(A+1, B):
            print(i, end = " ")
    elif A < B:
        print(B-A-1)
        for i in range(A+1, B):
            print(i, end = " ")
else:
    print(0)