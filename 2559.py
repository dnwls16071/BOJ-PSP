# 매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.
#
# 예를 들어, 아래와 같이 10일 간의 온도가 주어졌을 때,
#
# 3 -2 -4 -9 0 3 7 13 8 -3
#
# 모든 연속적인 이틀간의 온도의 합은 아래와 같다.
#
# 이때, 온도의 합이 가장 큰 값은 21이다.
#
# 또 다른 예로 위와 같은 온도가 주어졌을 때, 모든 연속적인 5일 간의 온도의 합은 아래와 같으며,
#
# 이때, 온도의 합이 가장 큰 값은 31이다.
#
# 매일 측정한 온도가 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오.

# code1
N, K = map(int, input().split())
temperature = list(map(int, input().split()))

sum_lst = []
for i in range(len(temperature)-K+1):
    sum_lst.append(sum(temperature[i:i+K]))
print(max(sum_lst))

# 그냥 간단해보였던 문제인데 답을 제출해보니 시간 초과가 출력되었다.
# 입력값 N, K가 최대 100000이 될 수 있기 때문에 for문을 돌면서 계속 더해주다보면 제한 시간을 넘길 수 있기 때문이다.

# code2
N, K = map(int, input().split())
temperature = list(map(int, input().split()))

temperature_part_sum = sum(temperature[:K])
result = [temperature_part_sum]

for i in range(0, len(temperature)-K):
    temperature_part_sum = temperature_part_sum - temperature[i] + temperature[i+K]
    result.append(temperature_part_sum)
print(max(result))

# ex. i = 0일때 가정하고 설명해보자.
# temperature_part_sum은 0~4일까지의 온도합을 초기값으로 설정한다.
# 그 다음 1~5일까지의 온도합을 구하려면 temperature_part_sum에다가 5일차 온도값을 더하고 0일차 온도값을 빼주면 된다.
# 따라서 코드를 작성해보면 temperature_part_sum += (temperature[i+K] - temperature[i])가 된다.