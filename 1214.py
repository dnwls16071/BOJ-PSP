# 구사과는 지폐를 오직 두 종류만 가지고 있다. 바로 P원 지폐와 Q원 지폐이다. 이 두 종류의 지폐를 구사과는 무한대만큼 가지고 있다.
#
# 오늘 구사과가 구매하려고 하는 물건의 가격은 D원이다. 구사과가 이 물건을 구매하기 위해서 지불해야 하는 금액의 최솟값은 얼마일까?
#
# 물건을 구매하기 위해서는 물건의 가격보다 크거나 같은 금액을 지불해야 한다.

D, P, Q = map(int, input().split())
if P < Q:
    P, Q = Q, P
min_cnt = (D // P + 1)  # 최소 개수 : D원을 P원 지폐로 모두 내는 경우
min_cost = min_cnt * P  # 최소 비용 : P원 지폐를 최소 개수만큼 지불하는 경우
if D % P == 0 or D % Q == 0:
    min_cost = D
else:
    for t in range(min_cnt - 1, -1, -1):
        div, mod = divmod(D - (t * P), Q)
        if mod == 0:
            min_cost = D
            break
        temp = (t * P) + ((div + 1) * Q)
        if temp == min_cost:
            break
        min_cost = min(min_cost, temp)  # 최소 비용과 중간값을 비교해서 최솟값을 최소 비용 변수에 저장한다.
print(min_cost)

# 그리디 알고리즘 스타일 성향을 약간 지니고있는 브루트포스 문제였다.
# 일반적인 최소 거스름돈 개수 문제보다는 살짝 생각할 것이 많았다.
