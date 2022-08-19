# "럭키스톤"은 카드를 통해 대결하는 게임이다. 창식이는 럭키스톤을 자주 한다.

# 이 게임의 카드에는 공격력과 생명력이 표시되어있다. 왼쪽에는 공격력이, 오른쪽에는 생명력이 숫자로 적혀있다.

# 서로 꺼낸 카드를 비교하여 남길 카드를 결정하는 데, 카드의 비교는 다음과 같이 이루어진다.

# 비교하는 카드의 공격력만큼 동시에 서로 상대 카드의 생명력을 깎는다. 줄어든 생명력은 다시 회복되지 않는다.
# 생명력이 0 이하인 경우에는 카드는 죽은 상태로 전환된다.
# 카드가 두 장 모두 남아있다면 비교를 계속한다.
# 요즘 따라 게임이 안 풀리는 창식이는 대전 전에 가능한 수를 미리 계산하여 최대한 이득을 챙기고 싶어 한다.

# 카드 2개의 공격력과 생명력이 주어지면 어떤 플레이어의 카드가 남아있을지 출력하는 프로그램을 작성해주자.

# 내가 작성한 코드
A_attack, A_defense = map(int, input().split())
B_attack, B_defense = map(int, input().split())

while 1:
    A_defense -= B_attack
    B_defense -= A_attack
    if A_defense <= 0 and B_defense <= 0:
        print("DRAW")
        break
    elif B_defense <= 0:
        print("PLAYER A")
        break
    elif A_defense <= 0:
        print("PLAYER B")
        break

# 비교 코드
a_power, a_life = map(int, input().split())
b_power, b_life = map(int, input().split())
while True:
    a_life -= b_power
    b_life -= a_power
    if a_life <= 0 and b_life <= 0:
        print('DRAW')
        break
    elif a_life <= 0:
        print('PLAYER B')
        break
    elif b_life <= 0:
        print('PLAYER A')
        break