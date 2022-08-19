# 준민이는 탄산 음료를 좋아한다. 탄산 음료를 사느라 돈을 다 써버렸기 때문에, 이제 준민이는 가진 돈이 없어 탄산 음료를 사먹을 수 없다.

# 준민이는 항상 법을 지키며 사는 사람이기 때문에, 아무리 탄산 음료가 먹고 싶어도 훔치지 않는다. 따라서, 법적으로 문제가 없는 방법으로 탄산 음료를 구매할 것이다.

# 마침 빈 병을 특정 개수만큼 가져가면, 새 병으로 바꾸어주는 이벤트가 진행중이다. 준민이는 길에서 빈 병을 열심히 찾은 뒤, 탄산 음료를 먹으려고 한다.

# 준민이가 현재 가지고 있는 빈 병의 수와 길에서 발견한 빈 병의 수, 새 병으로 바꾸는데 필요한 빈 병의 수가 주어졌을 때, 준민이가 탄산 음료를 몇 개 먹을 수 있는지 구하는 프로그램을 작성하시오.

e, f, c = map(int, input().split())

res = 0     # 마실 수 있는 콜라의 수
s = e + f   # 준민이가 가지고 있는 빈병의 수 + 그 날 발견한 빈병의 수 
while s >= c:   # 가지고 있는 병의 개수가 바꾸려고 하는 최소 병의 개수보다 크다면 계속 돌리기
    s -= c  # 콜라로 바꾸기 위해 필요한 병의 수만큼 차감
    res += 1  # 콜라 하나 추가
    s += 1 # 콜라를 다 마시고나면 빈병이 하나 추가됨
print(res)