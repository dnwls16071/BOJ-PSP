# 지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.
#
# 지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.
#
# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
# 큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

from collections import deque

N, M = map(int, input().split())
data = deque([i for i in range(1, N+1)])
lst = list(map(int, input().split()))

cnt = 0
for val in lst:
    while True:
        if data[0] == val:
            data.remove(data[0])
            break
        else:
            if data.index(val) <= (len(data) // 2):
                t = data.popleft()
                data.append(t)
                cnt += 1
            else:
                t = data.pop()
                data.appendleft(t)
                cnt += 1
print(cnt)

# 문제에서 '큐'라고 주어져서 리스트로 구현해야하나싶었는데 다시 보니 덱(deuqe)을 쓰면 훨씬 더 쉽게 구현할 수 있겠다고 판단했다.
# 찾는 수와 2, 3번 액션의 조건을 판단해서 작성해주면 매우 쉽게 풀 수 있었다.
