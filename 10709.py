# JOI시는 남북방향이 H 킬로미터, 동서방향이 W 킬로미터인 직사각형 모양이다. JOI시는 가로와 세로의 길이가 1킬로미터인 H × W 개의 작은 구역들로 나뉘어 있다. 북쪽으로부터 i 번째, 서쪽으로부터 j 번째에 있는 구역을 (i, j) 로 표시한다.

# 각 구역의 하늘에는 구름이 있을 수도, 없을 수도 있다. 모든 구름은 1분이 지날 때마다 1킬로미터씩 동쪽으로 이동한다. 오늘은 날씨가 정말 좋기 때문에 JOI시의 외부에서 구름이 이동해 오는 경우는 없다.

# 지금 각 구역의 하늘에 구름이 있는지 없는지를 알고 있다. 기상청에서 일하고 있는 여러분은 각 구역에 대해서 지금부터 몇 분뒤 처음으로 하늘에 구름이 오는지를 예측하는 일을 맡았다.

# 각 구역에 대해서 지금부터 몇 분뒤 처음으로 하늘에 구름이 오는지를 구하여라.

H, W = map(int, input().split())
for _ in range(H):
    cloud_location = input()
    c_idx = -1
    for i in range(W):
        if cloud_location[i] == "c":
            c_idx = i
            print(0, end = " ")
        elif c_idx == -1:
            print(-1, end = " ")
        else:
            print(i-c_idx, end = " ")
    print()


# # Blind tea tasting is the skill of identifying a tea by using only your senses of smell and taste.

# # As part of the Ideal Challenge of Pure-Tea Consumers (ICPC), a local TV show is organized. During the show, a full teapot is prepared and five contestants are handed a cup of tea each. The participants must smell, taste and assess the sample so as to identify the tea type, which can be: (1) white tea; (2) green tea; (3) black tea; or (4) herbal tea. At the end, the answers are checked to determine the number of correct guesses.

# # Given the actual tea type and the answers provided, determine the number of contestants who got the correct answer.

# T = int(input())
# contestant = list(map(int, input().split()))

# res = []
# for i in contestant:    
#     if i == T:
#         res.append(i)
# # print(len(res))