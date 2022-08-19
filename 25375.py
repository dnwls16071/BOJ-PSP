# 양의 정수 $a$, $b$가 주어지면, $gcd(x, y) = a$이고 $x + y = b$인 자연수 쌍 $(x, y)$가 존재하는지의 여부를 출력하자.

def gcd(x, y):
    while y != 0:
        remain = x % y
        x = y
        y = remain
    return x

Q = int(input())
for _ in range(Q):
    flag = 0
    a, b = map(int, input().split())
    x = 0
    y = b
    while x < y:
        if gcd(x, y) == a and x + y == b:
            flag = 1
            break
        else:
            x += 1
            y -= 1
    print(flag)