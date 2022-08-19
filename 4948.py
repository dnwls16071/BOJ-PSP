# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

def sosu(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


sosu_list = []
while True:
    sosu_list.clear()
    n = int(input())
    if n == 0:
        break

    if n == 1:
        print(1)

    if n > 1:
        for i in range(n + 1, 2 * n):
            if sosu(i):
                sosu_list.append(i)
        print(len(sosu_list))

# Python3로 제출한 결과 시간초과가 나왔는데 PyPy3로 제출한 결과 정답이 나왔다.
# 소수를 판별하는 함수를 만들 때 제곱근을 이용하여 범위를 최소화하는 방법을 이용하여 작성했다.