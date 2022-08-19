# 두 정수 A와 B를 입력받은 다음, A/B의 몫과 나머지를 출력하는 프로그램을 작성하시오.

# 어떤 정수 q와 r에 대해 A = qB + r (0 ≤ r < |B|)로 나타낼 수 있을 때, q를 몫, r을 나머지라고 한다.

# 내가 작성한 코드
# A, B = map(int, input().split())

# if A != 0 and A%B < 0:
#     quotient =  A//B + 1
#     remainder = A%B - B
# print(quotient)
# print(remainder)

# 참고한 코드
a, b = map(int,input().split())
c, d = a//b, a%b
if a != 0 and d < 0:
    c, d = c+1, d-b
print(c)
print(d)