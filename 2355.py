# 두 정수 A와 B가 주어졌을 때, 두 정수 사이에 있는 수의 합을 구하는 프로그램을 작성하시오. 사이에 있는 수들은 A와 B도 포함한다.

# 1차 작성한 코드(시간 초과)
A, B = map(int, input().split())

res = 0
for i in range(A, B+1):
    res += i
print(res)

# 2차 작성한 코드
A, B = map(int, input().split())

if A > B:
    A, B = B, A
if A < 0 and B >= 0:
    res = abs(A) + B + 1
elif A < 0 and B <= 0:
    res = abs(A-B) + 1
elif A >= 0 and B >= 0:
    res = abs(B-A) + 1

print(res*(A+B)//2)