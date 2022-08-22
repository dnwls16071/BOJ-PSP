# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 이분탐색을 활용한 코드
N = int(input())
array = list(map(int, input().split()))
lst = [0]

for arr in array:
    if arr > lst[-1]:
        lst.append(arr)
    else:
        left = 0
        right = len(lst)

        while left < right:
            mid = (left + right) // 2
            if lst[mid] < arr:
                left = mid + 1
            else:
                right = mid
        lst[right] = arr
print(len(lst)-1)

# 일반적인 다이나믹 프로그래밍을 이용한 코드
N = int(input())
lst = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))