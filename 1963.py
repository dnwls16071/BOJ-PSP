# 소수를 유난히도 좋아하는 창영이는 게임 아이디 비밀번호를 4자리 ‘소수’로 정해놓았다. 어느 날 창영이는 친한 친구와 대화를 나누었는데:
#
# “이제 슬슬 비번 바꿀 때도 됐잖아”
# “응 지금은 1033으로 해놨는데... 다음 소수를 무엇으로 할지 고민중이야"
# “그럼 8179로 해”
# “흠... 생각 좀 해볼게. 이 게임은 좀 이상해서 비밀번호를 한 번에 한 자리 밖에 못 바꾼단 말이야. 예를 들어 내가 첫 자리만 바꾸면 8033이 되니까 소수가 아니잖아. 여러 단계를 거쳐야 만들 수 있을 것 같은데... 예를 들면... 1033 1733 3733 3739 3779 8779 8179처럼 말이야.”
# “흠...역시 소수에 미쳤군. 그럼 아예 프로그램을 짜지 그래. 네 자리 소수 두 개를 입력받아서 바꾸는데 몇 단계나 필요한지 계산하게 말야.”
# “귀찮아”
# 그렇다. 그래서 여러분이 이 문제를 풀게 되었다. 입력은 항상 네 자리 소수만(1000 이상) 주어진다고 가정하자. 주어진 두 소수 A에서 B로 바꾸는 과정에서도 항상 네 자리 소수임을 유지해야 하고, ‘네 자리 수’라 하였기 때문에 0039 와 같은 1000 미만의 비밀번호는 허용되지 않는다.

import sys
from collections import deque
input = sys.stdin.readline

def findPrime():
    for i in range(2, 100):
        if prime[i]:
            for j in range(2*i, 10000, i):
                prime[j] = False

def BFS():
    queue = deque()
    queue.append([first, 0])
    visited = [0] * 10000
    visited[first] = 1
    while queue:
        current, cnt = queue.popleft()
        strCurrent = str(current)

        if current == last:
            return cnt
        for i in range(4):
            for j in range(10):
                ans = int(strCurrent[:i] + str(j) + strCurrent[i+1:])

                if visited[ans] == 0 and prime[ans] and ans >= 1000:
                    visited[ans] = 1
                    queue.append([ans, cnt + 1])

T = int(input())
prime = [True] * 10000
findPrime()
for _ in range(T):
    first, last = map(int, input().split())
    value = BFS()
    if value == None:
        print("Impossible")
    else:
        print(value)

# popleft() : 맨 앞의 원소를 pop시킨다.
# popleft()를 사용하면 하나의 원소만 나가는데  27행에서의 동작 방식이 이해가 되지 않아 따로 코드를 작성해서 확인해보았다.
# 만약 queue = deuqe([16, 5])라고 하자.

# while queue:
#     a, b = queue.popleft()
# print(a, b)

# 위와 같이 결과를 수행하면 결과는 16 5가 출력된다.