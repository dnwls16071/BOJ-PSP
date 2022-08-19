# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

N = int(input())

for i in range(1, N):
    print('*'*i + ' '*2*(N-i) + '*'*i)
for i in range(N, 0, -1):
    print('*'*i + ' '*2*(N-i) + '*'*i)

# n = int(input())
# for i in range(1, n):
#     print('*'*i + ' '*2*(n-i) + '*'*i)
# for i in range(n, 0, -1):
#     print('*'*i + ' '*2*(n-i) + '*'*i)