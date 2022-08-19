# 백준이는 작년 전국 대학생 프로그래밍 대회 동아리 연합(이하 전대프연) 회의에 불참했기 때문에, 올해 회장으로 선출되었다.

# 전대프연 회장은 오프라인 대회를 가을에 1회 개최해야 한다. 백준이는 대회를 개최할 주말을 마음대로 고를 수 있고, 회원들이 머무를 호텔을 찾아야 한다. 전대프연의 자금 사정은 넉넉하지 않기 때문에, 되도록 싼 호텔을 찾아야 한다.

# 여행의 총 비용은 예산을 초과하면 안 된다. 모든 회원은 같은 호텔에서 머물러야 한다. 작년에 모든 회원이 같은 호텔에 머무르지 않았고, 이로인해 대재앙이 일어났다. 일부 회원은 길을 잃어버렸고, 아직까지 그들을 다시 본 사람은 없다. 

a = list(map(int, input().split()))
N = a[0]    # 참가자 수
B = a[1]    # 예산
H = a[2]    # 호텔의 수
W = a[3]    # 고를수 있는 주

cost = list()   # 1인당 숙박 비용 저장
num_list = list()   # 주당 투숙 가능한 최대인원
can_list = list()   # 인원 수용 가능할 경우 비용
for i in range(H):
    c = input()
    cost.append(c)
    d = input()
    d = d.split()
    num_list.append(d)
    
for p in range(H):
    for k in num_list[p]:
        if int(k) > N:
            can_list.append(N * int(cost[p]))

if (len(can_list) == 0):
    print("stay home")
elif (min(can_list) > B):
    print("stay home")
else:
    print(min(can_list))