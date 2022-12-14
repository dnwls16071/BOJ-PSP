# 길이가 같은 두 단어가 주어졌을 때, 각 단어에 포함된 모든 글자의 알파벳 거리를 구하는 프로그램을 작성하시오.

# 두 글자 x와 y 사이의 알파벳 거리를 구하려면, 먼저 각 알파벳에 숫자를 할당해야 한다. 'A'=1, 'B' = 2, ..., 'Z' = 26. 그 다음 y ≥ x인 경우에는 y-x, y < x인 경우에는 (y+26) - x가 알파벳 거리가 된다.

# 예를 들어, 'B'와 'D' 사이의 거리는 4 - 2 = 2이고, 'D'와 'B' 사이의 거리는 (2+26) - 4 = 24이다.

# tip) 리스트를 일반 문자열 형태로 출력하는 아주 좋은 방법(단, 이 방법은 리스트의 원소가 숫자인 경우 가능한 방법)
# lst = [0, 1, 2, 3]

# print(lst) > 이렇게 작성하면 리스트형임을 알려주는 표시인 [](대괄호)가 같이 출력된다.
# print(*lst) > 하지만 출력하려는 리스트 앞에 *을 붙여주면 리스트형임을 알려주는 표시인 [](대괄호)가 출력되지않는다.


# 1차 작성한 코드(코드 에러)
T = int(input())

for _ in range(T):
    x, y = input().split()

    result = []
    for i in range(len(x)):
        if ord(x[i]) <= ord(y[i]):
            result.append(ord(y[i])-ord(x[i]))
        else:
            result.append((ord(y[i]) + 26) - ord(x[i]))
    print("Distances:", *result)
         
# # 2차 작성한 코드
# T = int(input())

# for _ in range(T):
#     a, b = input().split()
#     li = []
#     for i in range(len(a)):
#         if ord(a[i]) > ord(b[i]):
#             li.append(26 + ord(b[i]) - ord(a[i]))
#         else:
#             li.append(ord(b[i] - ord(a[i])))
#     print("Distances:", *li)