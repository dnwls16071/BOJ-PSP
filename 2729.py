# 이진수 덧셈은 매우 간단하고, 십진수 덧셈과 비슷하게 하면 된다. 십진수 덧셈을 할 때는, 오른쪽부터 왼쪽으로 차례대로 숫자 하나씩 더하면 된다. 이진수 덧셈도 이와 비슷하게 하면 된다. 십진수 덧셈은 외워야 할 덧셈이 많지만, 이진수 덧셈은 아래와 같이 5가지만 기억하면 된다.

# 0 + 0 = 0
# 1 + 0 = 1
# 0 + 1 = 1
# 1 + 1 = 10
# 1 + 1 + 1 = 11
# 두 이진수가 주어졌을 때, 그 합을 이진수로 출력하는 프로그램을 작성하시오.

T = int(input())

for i in range(T):
    a, b = map(str, input().split())
    a_int = 0
    a_cnt = 0
    for j in range(len(a)-1, -1, -1):
        a_int += int(a[j]) * (2**a_cnt)
        a_cnt += 1
    b_int = 0
    b_cnt = 0
    for k in range(len(b)-1, -1, -1):
        b_int += int(b[k]) * (2**b_cnt)
        b_cnt += 1
    res = a_int + b_int
    res = bin(res)
    res = str(res)
    print(res[2:])
    
    