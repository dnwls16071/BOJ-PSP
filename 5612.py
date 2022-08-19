# 상근이는 남산1호터널의 입구와 출구에서 1분에 통과하는 차량의 수를 조사했다. 이때, 터널에 차량이 가장 많이 있었을 때, 몇 대 있었는지 구하는 프로그램을 작성하시오.

n = int(input())
m = int(input())

max_car = 0
for i in range(n):
    a, b = map(int, input().split())
    m = m + a - b
    if m < 0:
        max_car = 0
        break
    
    if max_car < m:
        mar_car = m
print(max_car)