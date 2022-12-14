# 상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.

# 목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.

# 상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

# 1차 작성한 코드(틀렸습니다)
# N : 나무의 수, M : 상근이가 집으로 가져가려고 하는 나무의 길이
# N, M = map(int, input().split())
# # 나무의 높이
# tree_height = list(map(int, input().split()))

# # 시작점의 값은 0
# start = 0
# # 끝점의 값은 tree_height의 최댓값
# end = max(tree_height)

# # 절단기에 설정할 수 있는 높이의 최댓값
# result = 0
# # 가동 조건은 시작점이 끝점보다 항상 작거나 같아야지만 실행
# while (start <= end):
#     # 가져갈 수 있는 나무의 총 높이 합
#     total = 0
#     # 중간값 설정
#     mid = (start + end) // 2
#     # 나무의 높이를 요소로 하나하나 받아온다.
#     for i in tree_height:
#         # 만약 나무의 높이가 중간값보다 크다면?
#         if i > mid:
#             # 해당 나무의 높이에서 중간값을 뺀 나무의 높이를 더해준다.
#             total += i - mid
#     # 그런데 만약 총 높이의 합이 적어도 가져가야하는 M보다 작다면?
#     if total < M:
#         # 끝점의 값을 변경한다.
#         end = mid - 1
#     # 만약 총 높이의 합이 적어도 가져가야하는 M보다 크다면?
#     else:
#         # 절단기의 높이는 중간값으로 지정
#         result = mid
#         # 시작점의 값을 변경한다.
#         start = mid + 1

# print(result)

# 2차 작성한 코드(맞았습니다.)
N, M = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2

    total = 0
    for i in tree:
        if i >= mid:
            total += i - mid
    
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)