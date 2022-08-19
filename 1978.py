# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

N = int(input())    # 첫 줄에 수의 개수 N이 주어진다.

n = int(input())
nums = list(map(int, input().split()))
rescnt = 0

for i in nums:
    if i == 1:
        continue
    cnt = 0
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        rescnt += 1
print(rescnt)



