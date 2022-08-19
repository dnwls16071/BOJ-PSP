# 정수 N이 주어졌을 때, N의 제곱근을 구하는 프로그램을 작성하시오.

N = int(input())

start = 1
end = N

while True:
    mid = (start + end) // 2
    if mid**2 == N:
        print(mid)
        break
    elif mid**2 > N:
        end = mid - 1
    else:
        start = mid + 1

# 매우 큰 수에 대해서 math.sqrt()를 실행하게된다면 에러가 발생할 확률이 높다.
# 따라서 제곱근을 구할 때 이진탐색을 이용할 수 있다.
