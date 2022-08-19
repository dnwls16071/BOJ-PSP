# 오늘은 갑자기 주사위를 던지고 싶다.

# 그런데 코딩도 하고 싶다.

# 그럼 같이할까?

T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print("Case " + str(i) + ": " + str(A+B))