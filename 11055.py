# 수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

N = int(input())
a = list(map(int, input().split()))
b = []
for i in range(N):
    b.append(a[i])

for i in range(1, N):
    for j in range(i):
        if a[i] > a[j]:
            b[i] = max(b[i], b[j] + a[i])
print(max(b))

# 누적합을 구하기 위해서 똑같은 원소를 답은 리스트를 하나 더 만들었다.