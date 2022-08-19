# 10보다 작거나 같은 자연수 N개를 주면 합을 구하는 프로그램을 작성하시오.

# 1번 작성 코드
T = int(input()) #테스트 케이스의 개수

for _ in range(T):
    N = int(input())
    print(sum(map(int, input().split())))

# 2번 작성 코드
T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(sum(A))