# Given an odd integer N, calculate the sum of all the odd integers between 1 and N inclusive.

# 1차 작성한 코드
# T = int(input())

# for _ in range(T):
#     N = int(input())
#     print(sum([n for n in range(1, N+1) if n % 2]))

# 2차 작성한 코드
# 16행 코드문 설명 : 삼항연산자, 리스트내포를 이용한 코드
T = int(input())

for _ in range(T):
    N = int(input())
    num_list = [n for n in range(1, N+1) if n % 2 != 0]
    print(sum(num_list))