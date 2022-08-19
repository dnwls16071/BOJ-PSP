# 구사과의 방에는 난로가 하나 있다. 구사과는 절약 정신이 투철하기 때문에, 방에 혼자 있을 때는 난로를 되도록 켜지 않는다. 구사과는 방에 친구가 왔을 때는 항상 난로를 켠다.

# 오늘은 N명의 친구들이 구사과의 집에 방문하는 날이다. 구사과는 친구들을 쉽게 구분하기 위해 1부터 N까지 번호를 매겼다. i번째 친구는 구사과의 방에 시간 Ti에 도착하고, 시간 Ti+1에 나간다. 구사과의 방은 좁기 때문에, 한 번에 한 명만 방문할 수 있다. 즉, 방안에는 항상 구사과를 포함해 2명 이하의 사람만 있게 된다.

# 구사과는 난로를 아무 때나 켤 수 있고, 끌 수 있다. 난로를 켜려면 성냥을 이용해야 한다. 오늘 구사과는 총 K개의 성냥을 가지고 있다. 따라서, 최대 K번 난로를 켤 수 있다. 가장 처음에 난로는 꺼져있다.

# 구사과는 난로가 켜져 있는 시간을 최소로 하려고 한다. 구사과의 친구들이 도착하는 시간과 가지고 있는 성냥의 개수가 주어졌을 때, 난로가 켜져 있는 시간의 최솟값을 구하는 프로그램을 작성하시오.

# 친구의 수와 성냥의 수를 입력
N, K = map(int, input().split())

# 도착시간을 저장하는 리스트 생성
arrive_time = []
for _ in range(N):
    arrive_time.append(int(input()))

# 간격
diff_time = []
for i in range(len(arrive_time)-1):
    diff_time.append(arrive_time[i+1] - arrive_time[i])
diff_time.sort()

for _ in range(K-1):
    diff_time.pop()

for _ in range(K):
    diff_time.append(1)

print(sum(diff_time))