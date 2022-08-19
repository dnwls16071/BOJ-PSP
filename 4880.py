# 등차수열(AP)은 인접한 두 수의 차이(공차)가 일정한 수열이다. 예를 들어, 3, 5, 7, 9, 11, 13, ...은 차이가 2로 일정한 등차수열이다. 이 문제에서 등차수열의 공차는 항상 0이 아닌 정수이다.
#
# 등비수열(GP)는 각 항이 그 앞과 일정한 비(공비)를 가지는 수열이다. 예를 들어, 2, 6, 18, 54, ...은 공비가 3인 등비수열이다. 이 문제에서 등비수열의 공비는 항상 0이 아닌 정수이다.
#
# 어떤 수열의 연속한 세개의 숫자가 주어졌을 때, 이 수열이 등차수열인지 등비수열인지를 알아낸 뒤, 다음 항을 구하는 프로그램을 작성하시오.

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if b - a == c - b:  # 공차가 같다 = 등차수열
        print("AP", c + (c - b))
    else:   # 공비가 같다 == 등비수열
        print("GP", c * (c // b))

# ZeroDivisionError => 0으로 나눠지는 에러가 발생