# 두 양의 정수가 주어졌을 때, 첫 번째 수가 두 번째 수보다 큰지 구하는 프로그램을 작성하시오.

while True: #조건을 계속 만족한다면 계속 실행
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    if A > B:
        print("Yes")
    else:
        print("No")