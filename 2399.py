# 수직선에 n개의 점이 찍혀 있다. 각각의 점의 x좌표가 주어졌을 때, n2개의 모든 쌍에 대해서 거리를 더한 값을 구하는 프로그램을 작성하시오.
#
# 즉, 모든 i, j에 대해서 |x[i] - x[j]|의 합을 구하는 것이다.

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    x = list(map(int, input().split()))

    total = 0
    for i in range(n):
        for j in range(n):
            total += abs(x[i]-x[j])
    print(total)

