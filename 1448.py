# 세준이는 N개의 빨대를 가지고 있다. N개의 빨대 중에 3개의 빨대를 선택했을 때, 이 빨대로 삼각형을 만들 수 있다면, 세 변의 길이의 합의 최댓값을 구하고 싶다.

import sys
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort(reverse=True)

answer = -1 # 만약에 삼각형의 형성 조건을 부합하지 않는다면 출력해야하는값 -1
for i in range(N-2):
    if lst[i] < lst[i+1] + lst[i+2]:
        answer = lst[i] + lst[i+1] + lst[i+2]
        break
print(answer)