# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

X_nums = []
Y_nums = []

for i in range(3):
    x, y = map(int, input().split())
    X_nums.append(x)
    Y_nums.append(y)

for i in range(3):
    if X_nums.count(X_nums[i]) == 1:
        x4 = X_nums[i]
    elif Y_nums.count(Y_nums[i]) == 1:
        y4 = Y_nums[i]

print(x4, y4)


