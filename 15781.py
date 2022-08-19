# 배틀그라운드라는 게임에서는 머리와 몸을 보호하기 위해 헬멧과 조끼를 입는다. 

# 맵에는 다양한 헬멧과 조끼가 있으며 각각 방어력을 갖고 있다. 또한 최대 1개의 헬멧과 조끼밖에 입지 못한다. 경수는 배틀그라운드에서 승리하고 싶기 때문에 시간이 걸리더라도 최고의 헬멧과 조끼를 주워서 최대의 방어력을 얻고 싶어한다.

# 맵에 존재하는 조끼와 헬멧의 방어력이 주어졌을 때 경수를 도와 경수가 얻을 수 있는 방어력의 최댓값을 구해주자.

N, M = map(int, input().split())    # 맵에 존재하는 헬멧의 개수 N과 조끼의 개수 M
H = list(map(int, input().split()))
A = list(map(int, input().split()))

H_max = max(H)
A_max = max(A)

print(H_max + A_max)