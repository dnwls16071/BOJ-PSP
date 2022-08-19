# 앞 면에 O와 X가 적혀있는 카드 N개가 있다. N개의 카드 중 M개의 카드의 앞면에는 O가 한 개 적혀있고, 나머지 N-M개의 카드의 앞면에는 X가 한 개 적혀있다. 카드의 뒷 면은 두 종류의 카드 모두 같은 모양이라 구분할 수 없다.

# 카드의 뒷 면에 O나 X를 하나씩 적으려고 한다. 이 때, O는 K개, X는 N-K개 적으려고 한다.

# 앞 면과 뒷 면에 같은 모양이 적혀있는 카드의 최대 개수를 구하는 프로그램을 작성하시오

N, M, K = map(int, input().split())

UP_lst = []
for _ in range(M):
    UP_lst.append("O")
for _ in range(N-M):
    UP_lst.append("X")

DOWN_lst = []
for _ in range(K):
    DOWN_lst.append("O")
for _ in range(N-K):
    DOWN_lst.append("X")

ans = 0
for i in range(N):
    if UP_lst[i] == DOWN_lst[i]:
        ans += 1
print(ans)














# # 두 개의 바구니에 사과와 오렌지가 있다. 첫 번째 바구니에는 사과 A개와 오렌지 B개가 있으며 두 번째 바구니에는 사과 C개와 오렌지 D개가 있다.

# # 당신은 한 바구니에 있는 과일 하나를 집어서 다른 바구니로 옮길 수 있다. 이런 식으로 과일을 옮길 때, 한 바구니에는 사과만 있게 하고 다른 쪽에는 오렌지만 있게 하려고 한다.

# # 앞서 말한 조건을 만족하도록 과일을 옮길 때, 과일을 옮기는 최소 횟수를 구하는 프로그램을 작성하여라.

# A, B = map(int, input().split())
# C, D = map(int, input().split())

# print(min(A+D, B+C))