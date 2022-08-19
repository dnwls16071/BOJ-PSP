# n개의 원소 중에서 k개를 순서 없이 선택하는 방법의 수는 몇 가지 일까?

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if b > a - b:   # ex. 49C1 = 49C48인 경우 좌변 형태로 변형
        b = a - b
    total = 1
    for i in range(1, b+1):
        total = total * a // i  # ex. 49C2 = (49 * 48) // (2 * 1)
        a -= 1
    print(total)

# 조합론 문제를 풀 때 시간복잡도와 공간복잡도를 고려하지않는다면 바로 itertools를 사용해서 간단하게 문제를 풀 수 있다.
# 하지만 시간복잡도와 공간복잡도를 고려해야한다면 itertools로 사용해서 풀 수 없다.
# 이럴때는 사람이 직접 조합을 계산하는것처럼 계산 로직을 짜야한다.
