# You are grading an arithmetic quiz. The quiz asks a student for the sum of the numbers. Determine if the student taking the quiz got the question correct.

A, op1, B, op2, C = map(str, input().split())
A = int(A)
B = int(B)
C = int(C)
if op1 == "+":
    tmp = A + B
    if tmp == C:
        print("YES")
    else:
        print("NO")
elif op1 == "-":
    tmp = A - B
    if tmp == C:
        print("YES")
    else:
        print("NO")
elif op1 == "*":
    tmp = A*B
    if tmp == C:
        print("YES")
    else:
        print("NO")
elif op1 == "/":
    tmp = int(A/B)
    if tmp == C:
        print("YES")
    else:
        print("NO")