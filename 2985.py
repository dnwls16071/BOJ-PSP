# 수학을 못해도 너무 못하는 상근이는 정인이에게 과외를 받고 있다. 오늘은 상근이가 사칙연산을 배우는 날이다.

# 정인이는 공책에 숫자 세개로 이루어진 등식을 적어주었다. (식은 자연수와 등호(=), 그리고 더하기, 빼기, 곱하기, 나누기 기호(+-*/)로 이루어져 있다)

# 상근이는 이런 등식을 사칙연산을 모르는 창영이게 자랑하다가 그만... 창영이는 숫자를 제외한 기호를 모두 지워버리고 말았다.

# 세 정수가 주어졌을 때, 원래 정인이가 적어준 등식을 구하는 프로그램을 작성하시오.

A, B, C = map(int, input().split())

if A + B == C:
    print(str(A) + "+" + str(B) + "=" + str(C))
elif A - B == C:
    print(str(A) + "-" + str(B) + "=" + str(C))
elif A / B == C:
    print(str(A) + "/" + str(B) + "=" + str(C))
elif A * B == C:
    print(str(A) + "*" + str(B) + "=" + str(C))
elif A == B + C:
    print(str(A) + "=" + str(B) + "+" + str(C))
elif A == B - C:
    print(str(A) + "=" + str(B) + "-" + str(C))
elif A == B * C:
    print(str(A) + "=" + str(B) + "*" + str(C))
elif A == B / C:
    print(str(A) + "=" + str(B) + "/" + str(C))
    
