# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# # 1차 작성 코드
# N, K = list(map(int, input().split()))
# coin_list = list()

# for i in range(N):
#     coin_list.append(int(input()))
# coin_list.sort(reversed=True)

# count = 0
# for i in range(N):
#     count += K // coin_list[i]
#     K = K % coin_list[i]
# print(count)

# 2차 작성 코드
N, K = list(map(int, input().split()))
coin_list = []

for i in range(N):
    coin_list.append(int(input()))

count = 0
# range(N, 0, -1) 이 방법과 동일한 reversed(range(N))
for i in range(N, -1, -1):
# for i in reversed(range(N)):
    count += K // coin_list[i]
    K = K % coin_list[i]
print(count)

