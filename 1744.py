# 길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다. 하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다. 어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다. 하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다. 그리고 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.
#
# 예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다. 하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.
#
# 수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.
#
# 수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.

N = int(input())
positive_num = []
negative_num = []
max_sum = 0
for _ in range(N):
    n = int(input())
    if n > 1:
        positive_num.append(n)
    elif n == 1:
        max_sum += 1
    else:
        negative_num.append(n)

positive_num.sort(reverse=True)
negative_num.sort()

if len(positive_num) % 2 == 0:
    for i in range(0, len(positive_num), 2):
        max_sum += positive_num[i] * positive_num[i + 1]
else:
    for i in range(0, len(positive_num) - 1, 2):
        max_sum += positive_num[i] * positive_num[i + 1]
    max_sum += positive_num[-1]

if len(negative_num) % 2 == 0:
    for i in range(0, len(negative_num), 2):
        max_sum += negative_num[i] * negative_num[i + 1]
else:
    for i in range(0, len(negative_num) - 1, 2):
        max_sum += negative_num[i] * negative_num[i + 1]
    max_sum += negative_num[-1]
print(max_sum)

# 음수, 양수를 따로 구분해서 저장한다.
# 작은 음수끼리 곱해줘야 큰 값이 나오고 큰 양수끼리 곱해줘야 큰 값이 나온다.
# 음수를 정렬할때는 오름차순, 양수를 정렬할때는 내림차순으로 정렬한다.
# 0을 양수랑 곱하게 되면 오히려 값이 작아지게 되므로 0을 음수랑 곱하는 방식을 택해서 값을 오히려 크게 만들어준다.
