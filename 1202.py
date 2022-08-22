# 세계적인 도둑 상덕이는 보석점을 털기로 결심했다.

# 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.

# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

# 훔칠 수 있는 보석의 최대 가격
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewelry = []
for _ in range(N):
    heapq.heappush(jewelry, list(map(int, input().split())))
bag = []
for _ in range(K):
    bag.append(int(input()))
bag.sort()

total = 0
temp = []
for i in bag:
    while jewelry and i >= jewelry[0][0]:
        M, V = heapq.heappop(jewelry)
        heapq.heappush(temp, -V)
    if temp:
        total -= heapq.heappop(temp)
print(total)

# 냅색 알고리즘과 비슷한 유형의 문제였다.

# -를 붙여서 최대힙을 구현한다.
# i = 2kg일때 2kg >= 1kg이므로 65원의 보석을 넣을 수 있다.
# i = 2kg일때 2kg >= 2kg이므로 99원의 보석을 넣을 수 있다.
# i = 2kg일때 2kg < 5kg이므로 X

# 이때 한 가방에는 최대 한 보석만 넣을 수 있으므로 값이 가장 작은 값을 리턴해주는 heapq.heappop()를 사용한다.
# i = 2kg 가방에는 99원의 보석을 넣는다.(왜냐면 최대힙을 구현하기 위해서 음수로 처리했기때문)

# i = 10kg일때 10kg >= 5kg이므로 23원의 보석을 넣을 수 있다.

# 이때 한 가방에는 최대 한 보석만 넣을 수 있으므로 가장 작은 값을 리턴해주는 heapq.heappop()를 사용한다.
# = 10kg 가방에는 65원의 보석을 넣는다.(왜냐면 최대힙을 구현하기 위해서 음수로 처리했기때문)

# 위 문제와 반대로 최소힙을 구현하려면 어떻게 코드를 작성해야할지 고민하면서 아래와 같이 코드를 바꿔 작성해보았다.
# 훔칠 수 있는 보석의 최소 가격
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewelry = []
for _ in range(N):
    heapq.heappush(jewelry, list(map(int, input().split())))
bag = []
for _ in range(K):
    bag.append(int(input()))
bag.sort()

total = 0
temp = []
for i in bag:
    while jewelry and i >= jewelry[0][0]:
        M, V = heapq.heappop(jewelry)
        heapq.heappush(temp, V)
    if temp:
        total += heapq.heappop(temp)
print(total)

# 가장 작은 값을 리턴해주는 heapq.heappop()를 사용하므로 양수에서는 그대로 작은 값을 출력한다.
# 가장 작은 값을 리턴해주는 heapq.heappop()를 사용하므로 음수에서는 (-)부호를 붙여 작은 값을 출력한다.

# 처음에 이 문제를 풀려고 했을때 아예 감조차 잡히지 않았고 대충 파악하는 정도였다.(정렬 사용)
# 우선순위 큐에 대해서 자세하게 알게 되었다. 좀 더 많이 이용해보자.