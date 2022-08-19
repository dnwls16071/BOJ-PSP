# 덧셈, 뺄셈, 곱셈, 나눗셈을 할 수 있는 계산기 프로그램을 만드시오.

res = int(input())
while True:
    op = input()
    if op == "=":
        break
    
    n = int(input())
    if op == "+":
        res += n
    elif op == "-":
        res -= n
    elif op == "*":
        res *= n
    elif op == "/":
        res //= n
print(res)