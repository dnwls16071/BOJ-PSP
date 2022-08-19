# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

S = int(input())

result = 0
n = 1

while 1:
    result += n
    if result > S:
        n -= 1
        break
    else:
        n += 1

print(n)