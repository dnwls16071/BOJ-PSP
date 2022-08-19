# n개의 자연수로 이루어진 수열이 주어질 때, 특정 구간 [i,j](i≤j)의 합이 k보다 큰 모든 쌍 i,j의 개수를 출력하시오.

# 1차 코드(시간초과)
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if sum(arr[i:j+1]) > k:
            cnt += 1
print(cnt) 