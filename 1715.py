# 정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다. 이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.
#
# 매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라서 비교 횟수가 매우 달라진다. 예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다. 그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.
#
# N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.

import heapq

N = int(input())
card = []
for _ in range(N):
    card.append(int(input()))
heapq.heapify(card)

res = 0
while len(card) != 1:
    num1 = heapq.heappop(card)
    num2 = heapq.heappop(card)
    num3 = num1 + num2
    res += num3
    heapq.heappush(card, num3)
print(res)

# 문제 이해는 쉬웠는데 어떻게 구현해야할지 잘 몰랐다.
# 이런 부류의 문제는 힙을 이용해서 코드를 작성할 수 있다는 것을 알게 되었다.

# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
# heapq.heapify() : 이미 원소가 들어있는 리스트를 힙 형태로 변환

