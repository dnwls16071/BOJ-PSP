# 중간계에 전쟁이 일어나려고 한다. 간달프는 사우론에 대항하기 위한 군대를 소집했고, 여러 종족이 이 군대에 가담했다. 전쟁을 시작하기 전에 간달프는 각 종족에 점수를 매겼다.

# 간달프의 군대의 각 종족의 점수는 다음과 같다.

# 호빗 - 1
# 인간 - 2
# 엘프 - 3
# 드워프 - 3
# 독수리 - 4
# 마법사 - 10
# 사우론의 군대의 점수는 다음과 같다.

# 오크 - 1
# 인간 - 2
# 워그(늑대) - 2
# 고블린 - 2
# 우럭하이 - 3
# 트롤 - 5
# 마법사 - 10
# 중간계는 매우 신비한 곳이어서 각 전투의 승리는 날씨, 장소, 용맹에 영향을 받지 않는다. 전투에 참여한 각 종족의 점수를 합한 뒤, 큰 쪽이 이긴다.

# 전투에 참여한 종족의 수가 주어졌을 때, 어느 쪽이 이기는지 구하는 프로그램을 작성하시오.

T = int(input())
cnt = 1
for _ in range(T):
    first_troop = list(map(int, input().split()))
    second_troop = list(map(int, input().split()))
    first_troop_score = first_troop[0]*1 +first_troop[1]*2 + first_troop[2]*3 + first_troop[3]*3 + first_troop[4]*4 + first_troop[5]*10
    second_troop_score = second_troop[0]*1 + second_troop[1]*2 + second_troop[2]*2 + second_troop[3]*2 + second_troop[4]*3 + second_troop[5]*5 + second_troop[6]*10

    if first_troop_score > second_troop_score:
        print("Battle " + str(cnt) + ":", "Good triumphs over Evil")
        cnt += 1
    elif first_troop_score < second_troop_score:
        print("Battle " + str(cnt) + ":", "Evil eradicates all trace of Good")
        cnt += 1
    else:
        print("Battle " + str(cnt) + ":", "No victor on this battle field")
        cnt += 1