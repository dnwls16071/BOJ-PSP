# 승택이의 아들이 생일을 맞았다. 승택이는 아들을 위해 생일 파티를 하려고 한다.

# 하지만 아들의 친구들을 모두 초대할 수는 없다. 아이들에게 나눠 줄 사탕이 부족하기 때문이다.

# 아이들은 항상 한 종류의 사탕만을 먹고 싶어한다. 게다가, 한 종류의 사탕을 최소한 K개 이상 먹어야만 행복해한다.

# K가 주어지고 승택이가 현재 갖고 있는 사탕의 종류와 개수가 주어진다. 이때, 생일파티에 올 수 있는 아이들은 최대 몇 명일까?

# 1차 작성한 코드
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    
    res = 0
    for i in lst:
        res += (i // K)
    print(res)