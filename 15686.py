# 크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.

# 이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다. 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

# 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

# 예를 들어, 아래와 같은 지도를 갖는 도시를 살펴보자.

# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 1
# 0 0 0 1 2
# 0은 빈 칸, 1은 집, 2는 치킨집이다.

# (2, 1)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |2-1| + |1-2| = 2, (5, 5)에 있는 치킨집과의 거리는 |2-5| + |1-5| = 7이다. 따라서, (2, 1)에 있는 집의 치킨 거리는 2이다.

# (5, 4)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |5-1| + |4-2| = 6, (5, 5)에 있는 치킨집과의 거리는 |5-5| + |4-5| = 1이다. 따라서, (5, 4)에 있는 집의 치킨 거리는 1이다.

# 이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다. 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 한다. 오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개라는 사실을 알아내었다.

# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.

if __name__ == "__main__":
    from itertools import combinations
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    house = []
    chicken = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                house.append((i, j))
            if board[i][j] == 2:
                chicken.append((i, j))
    
    min_distance = 15000
    for ch in combinations(chicken, M):
        sum_distance = 0
        for ho in house:
            sum_distance += min([abs(ho[0]-i[0]) + abs(ho[1]-i[1]) for i in ch])
            if min_distance <= sum_distance:
                break
        if min_distance > sum_distance:
            min_distance = sum_distance
    print(min_distance)

# 2차원 배열의 값이 1인 경우 집 리스트에 저장
# 2차원 배열의 값이 2인 경우 치킨집 리스트에 저장
# 치킨집과 각 집 사이의 거리가 최소가 되게끔 사업을 시작해야 치킨거리가 최소가 될 수 있다.
# 하나의 집과 조합을 이용한 치킨집 리스트를 하나씩 가져와 절댓값으로 연산하여 거리를 측정하고 그 값들 중에서 가장 최솟값을 택한다.
# 치킨거리의 합이 최소거리보다 크다면 그것은 답이 될 수 없다.
# 치킨거리의 합이 최소거리보다 더 작다면 구하고자하는 치킨거리가 되기에 정답이 된다.

# 이 문제는 삼성SW역량테스트 문제로 출제되었던 문제이다.
# 처음에 이 문제를 이해하는것은 간단했지만 코드를 어떻게 구현할지 막막했다.
# 뿐만 아니라 잦은 실수로 인해 문제를 푸는데 꽤 오랜시간이 걸려서 풀고 나서도 매우 아쉬운 기분이 들었다. 

if __name__ == "__main__":
    from itertools import combinations
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    house = []
    chicken = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                house.append([i, j])
            if board[i][j] == 2:
                chicken.append([i, j])
    
    min_distance = 15000
    for ch in combinations(chicken, M):
        sum_distance = 0
        tmp = []
        for ho in house:
            tmp.append(abs(ch[0]-ho[0]) + abs(ch[1]-ho[1]))
        sum_distance += min(tmp)
        if min_distance <= sum_distance:
            break
        if min_distance > sum_distance:
            min_distance = sum_distance 
    print(min_distance)       