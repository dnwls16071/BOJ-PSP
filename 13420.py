# 사칙연산은 덧셈, 뺄셈, 곱셈, 나눗셈으로 이루어져 있으며, 컴퓨터 프로그램에서 이를 표현하는 기호는 +, -, *, / 와 같다. 아래는 컴퓨터 프로그램에서 표현한 사칙 연산의 예제이다.

# 3 * 2 = 6

# 문제와 답이 주어졌을 때, 이를 계산하여 올바른 수식인지 계산하는 프로그램을 만들려고 한다. 만약 주어진 데이터가 3 * 2 = 6 이라면 정답으로, 3 * 2 = 7 이면 오답으로 채점을 하면 된다. 문제와 답이 주어졌을 때, 이를 채점하는 프로그램을 작성하시오.

T = int(input())
for i in range(T):
    A, op1, B, op2, C = map(str, input().split())
    A, B, C = int(A), int(B), int(C)
    if op1 == "+":
        tmp = A + B
        if tmp == C:
            res = "correct"
        else:
            res = "wrong answer"
    elif op1 == "-":
        tmp = A - B
        if tmp == C:                   
            res = "correct"
        else:
            res = "wrong answer"
    elif op1 == "*":
        tmp = A * B
        if tmp == C:
            res = "correct"
        else:
            res = "wrong answer"
    elif op1 == "/":
        tmp = int(A/B)
        if tmp == C:
            res = "correct"
        else:
            res = "wrong answer"
    print(res)

    