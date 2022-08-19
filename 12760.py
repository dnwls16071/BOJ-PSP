# 수많은 토너먼트를 거쳐 최종 플레이어 \(N\)명이 남아있다. 각 플레이어는 \(M\)장씩의 숫자가 적힌 카드를 가지고 있으며, 이들은 매 턴 자신이 가진 카드 중 가장 큰 카드를 두고 비교를 하는데, 그 카드들 중 가장 큰 수를 가진 플레이어가 1점을 획득한다. 그 턴에 사용된 카드는 버리기로 한다. 가장 큰 수를 가진 플레이어는 여러 명일 수 있다. \(M\)번의 경기 후 가장 많은 점수를 획득한 플레이어는 몇 번 플레이어인가?

N, M = map(int, input().split())
player = []
for _ in range(N):
    lst = sorted(list(map(int, input().split())), reverse=True)
    player.append(lst)

ranking = [0] * N

for i in range(M):
    max_num = player[0][i]
    for j in range(N):
        max_num = max(max_num, player[j][i])
    for j in range(N):
        if player[j][i] == max_num:
            ranking[j] += 1

result = []
for i in range(len(ranking)):
    if max(ranking) == ranking[i]:
        result.append(i+1)
print(*result)

# 문제이해는 쉬웠으나 구현하는데 시간이 좀 걸렸던 문제였다.
# 우선 입력값 그대로 카드를 내야한다는 조건이 없기 때문에 입력리스트를 내림차순 정렬해서 플레이어 리스트에 추가하였다.
# 첫 번째 플레이어의 i번째 카드를 최댓값으로 설정하고 다른 플레이어와 카드를 비교해서 최댓값을 갱신한다.
# j번째 플레이어의 i번째 카드를 최댓값과 비교했을때 같다면 ranking 배열에서 해당 플레이어의 값을 증가시킨다.