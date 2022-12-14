# 영관이는 게임을 좋아한다. 별의별 게임을 다 하지만 그 중에서 제일 좋아하는 게임은 모두의 마블이다. 어김없이 오늘도 영관이는 학교 가는 버스에서 캐릭터 합성 이벤트를 참여했다.
#
# 이번 이벤트는 다음과 같다. 순서가 매겨진 여러 장의 카드가 있다. 각각의 카드는 저마다 레벨이 있다.
#
# 카드 A에 카드 B를 덧붙일 수 있다. 이때 붙이는 조건은 다음과 같다.
#
# 두 카드는 인접한 카드여야 한다.
# 업그레이드 된 카드 A의 레벨은 변하지 않는다.
# 카드 합성을 할 때마다 두 카드 레벨의 합만큼 골드를 받는다.
#
# 영관이가 골드를 최대한 많이 받을 수 있게 여러분이 도와주자.
#
# 예를 들어, c1, c2, c3로 연속된 카드 3개가 있고 각각 레벨이 40,30,30 이라고 하자.
#
# 이 카드들을 합치는 과정에서, 먼저 c3에 c2를 합쳐 임시 카드 x1을 만든다. x1의 레벨은 30이고 획득 골드는 60이다. 그 다음엔 c1에 x1을 합쳐 카드 x2를 만들면 레벨이 40이고 70만큼의 골드를 획득할 수 있다. 이때, 영관이가 획득한 골드는 70+60 = 130이다.
#
# 다른 방법으로 c1에 c2를 덧붙인 카드 x1을 만들면, x1의 레벨은 40이고 획득한 골드는 70이다.
#
# x1에 c3를 덧붙인 카드 x2의 레벨은 40이고 획득 골드는 70이다. 이때, 영관이가 획득한 골드는 70 + 70 = 140이다. 이외에 더 많은 골드를 받는 방법이 없으므로 140이 획득할 수 있는 최대 골드이다.

# Code1
import sys
input = sys.stdin.readline
n = int(input())
level = list(map(int, input().split()))
level.sort(reverse=True)

gold = []
while True:
    if len(level) == 1:
        break
    gold.append(level[0] + level[1])
    level.remove(level[1])
print(sum(gold))

# Code2
n = int(input())
level = list(map(int, input().split()))
level.sort(reverse=True)

gold = 0
for i in range(len(level)):
    if i <= 1:
        gold += level[i]
    else:
        gold += level[0] + level[i]
print(gold)

# 처음에 Code1으로 제출했는데 시간초과가 나왔다.
# Code2로 제출하여 RA를 받았고 그 다음에 Code1을 다시 수정해보았다.
# Code1, Code2 모두 Python3, PyPy3 둘 다 통과했다.
