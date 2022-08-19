# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()

start = 0
end = n - 1

cnt = 0
while start < end:  # ( = ) 의 경우는 제외
    if arr[start] + arr[end] == x:
       cnt += 1
       start += 1
       end -= 1
    elif arr[start] + arr[end] > x:
        end -= 1
    elif arr[start] + arr[end] < x:
        start += 1
print(cnt)