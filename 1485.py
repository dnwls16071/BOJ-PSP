# 네 점이 주어졌을 때, 네 점을 이용해 정사각형을 만들 수 있는지 없는지를 구하는 프로그램을 작성하시오.

def square(c):
    side_one = (c[0][0] - c[1][0])**2 + (c[0][1] - c[1][1])**2
    side_two = (c[1][0] - c[3][0])**2 + (c[1][1] - c[3][1])**2
    side_three = (c[3][0] - c[2][0])**2 + (c[3][1] - c[2][1])**2
    side_four = (c[2][0] - c[0][0])**2 + (c[2][1] - c[0][1])**2

    diagonal_one = (c[0][0] - c[3][0])**2 + (c[0][1] - c[3][1])**2
    diagonal_two = (c[2][0] - c[1][0])**2 + (c[2][1] - c[1][1])**2

    if side_one != side_two:
        return 0
    if side_three != side_four:
        return 0
    if diagonal_one != diagonal_two:
        return 0
    return 1

T = int(input())
for i in range(T):
    lst = []
    for _ in range(4):
        a, b = list(map(int, input().split()))
        lst.append((a, b))
    lst.sort(key = lambda x : (x[0], x[1]))
    print(square(lst))

# 이 문제는 수학 중에서도 기하학 문제에 속하는 아주 기초적인 문제이다.
# 정사각형의 성립 조건을 생각해보면 다음과 같이 두 가지가 있다.

# 1. 사각형의 네 변의 길이가 모두 같아야 한다.
# 2. 두 대각선의 길이 역시 모두 같아야 한다.

# 리스트에 튜플 형식으로 저장한 다음에 sort, key = lambda를 통해서 정렬할 수 있다.
# lst.sort(key = lambda x : (x[0], x[1])) => 매개변수의 첫 번째 값 기준으로 오름차순 정렬, 첫 번째 값이 같은 경우에는 두 번째 값을 기준으로 오름차순 정렬한다.
# 정렬할때 무조건 리스트 형식으로 저장하지않고 위와 같이 튜플로도 저장해서 정렬할 수 있다는 것을 알게 되었다.
