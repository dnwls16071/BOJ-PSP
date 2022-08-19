# 컴퓨터를 이용하면 수학 계산이 조금 쉬워진다. 다음과 같은 예를 살펴보자. 세 변의 길이가 a, b, c(c는 빗변)이면서 a2+b2=c2를 만족하는 삼각형을 직각삼각형이라고 한다. 이 공식은 피타고라스의 법칙이라고 한다.

# 직각 삼각형의 두 변의 길이가 주어졌을 때, 한 변의 길이를 구하는 프로그램을 작성하시오.

cnt = 1
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    
    # if문은 분기문으로 순차적으로 내려가므로 직각삼각형이 형성되지않는 조건을 먼저 입력하고
    # 그 뒤에 각각의 경우를 가정하여 코드를 작성해야한다.
    if c == -1:
        print("Triangle #" + str(cnt))
        print("c = " + "%.3f" % ((a**2+b**2)**0.5))
    # 빗변보다 큰 값이 a, b에서 나와버리면 직각삼각형이 형성되지 않기 때문에
    elif max(a, b) >= c:
        print("Triangle #" + str(cnt))
        print("Impossible.")
    elif b == -1:
        print("Triangle #" + str(cnt))
        print("b = " + "%.3f" % ((c**2-a**2)**0.5))
    elif a == -1:
        print("Triangle #" + str(cnt))
        print("a = " + "%.3f" % ((c**2-b**2)**0.5))

    cnt += 1
    # 줄 바꿈 출력
    print()