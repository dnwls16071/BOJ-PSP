# 꿍은 오늘 학교에서 삼각형에 대해 배웠다. 삼각형은 변의 길이에 따라 다음과 같이 분류될 수 있다.

# 정삼각형(equilateral triangle)은 모든 변의 길이가 같다. 각 역시 60도로 모두 같다.
# 이등변삼각형(isosceles triangle)은 두 개의 변의 길이가 같다. 각 역시 두 개의 각의 크기가 같다.
# 부등변삼각형(scalene triangle)은 모든 변의 길이가 같지 않다. 각 역시 모두 다르다. 몇몇 부등변삼각형의 경우 직각삼각형이다.
# 수학선생님이 삼각형의 세 변의 길이를 가지고 삼각형을 분류하라는 숙제를 내줬는데 꿍은 정말 놀고싶다. 꿍이 놀수있도록 여러분이 도와주어라.

T = int(input())

cnt = 1
for i in range(T):
    lst = sorted(map(int, input().split()))
    if lst[0] + lst[1] <= lst[2]:
        print("Case " + "#" + str(cnt) + ":" + " invalid!")
    elif lst[0] == lst[1] == lst[2]:
        print("Case " + "#" + str(cnt) + ":" + " equilateral")
    elif lst[0] == lst[1] or lst[0] == lst[2] or lst[1] == lst[2]:
        print("Case " + "#" + str(cnt) + ":" + " isosceles")
    else:
        print("Case " + "#" + str(cnt) + ":" + " scalene")
    
    cnt += 1

        