# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

N, M = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = 0

cnt = 0
while start < N and end < N:
    if sum(lst[start:end+1]) < M:
        end += 1
    elif sum(lst[start:end+1]) == M:
        cnt += 1
        if start < end:
            start += 1
        else:
            end += 1
    else:
        start += 1
print(cnt)

# 투 포인터 유형 정리
# 양쪽 끝에서 시작하는 유형1
# 같은 위치에서 시작하면서 경우에 따라 포인터의 값이 증가하는 유형2
