# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.

# 도현이는 앞으로 M번 공을 바꾸려고 한다. 도현이는 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환한다.

# 공을 어떻게 바꿀지가 주어졌을 때, M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램을 작성하시오.

N, M = map(int, input().split())
baskets = [i for i in range(1, N+1)]

for _ in range(M):
    a, b = map(lambda x:int(x)-1, input().split())
    baskets[a], baskets[b] = baskets[b], baskets[a]

print(*baskets)

# 코드 설명
# a, b = map(lambda x:int(x)-1, input().split()) 
# ex) a = 1, b = 2를 인자로 받아오는 경우를 생각해보자.
# 먼저 a = 1을 받아온다면 lambda 함수를 거쳐 실제로 리턴되는 값은 0
# 그 뒤로 b = 2를 받아온다면 lambda 함수를 거쳐 실제로 리턴되는 값은 1

# lambda 함수를 이용한 정렬
# print(key= lambda x:(x[0], x[1]) > 우선순위에 따른 정렬