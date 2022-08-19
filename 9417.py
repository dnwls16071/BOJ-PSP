# 정수 M개가 주어졌을 때, 모든 두 수의 쌍 중에서 가장 큰 최대공약수 찾는 프로그램을 작성하시오.

def GCD(a, b):
    while b != 0:
        remain = a % b
        a = b
        b = remain
    return a

N = int(input())
for _ in range(N):
    lst = list(map(int, input().split()))
    max_num = 0
    for a in range(len(lst)):
        for b in range(a+1, len(lst)):
            if max_num < GCD(lst[a], lst[b]):
                max_num = GCD(lst[a], lst[b])
    print(max_num)

# 최대공약수, 최소공배수 문제라서 유클리드 호제법을 먼저 떠올렸다.
# 최대공약수를 구하는 함수를 작성하고 이중반복문을 통해서 구현했다.
