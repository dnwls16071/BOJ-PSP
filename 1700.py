# 기숙사에서 살고 있는 준규는 한 개의 멀티탭을 이용하고 있다. 준규는 키보드, 헤어드라이기, 핸드폰 충전기, 디지털 카메라 충전기 등 여러 개의 전기용품을 사용하면서 어쩔 수 없이 각종 전기용품의 플러그를 뺐다 꽂았다 하는 불편함을 겪고 있다. 그래서 준규는 자신의 생활 패턴을 분석하여, 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고, 이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안하여 보다 쾌적한 생활환경을 만들려고 한다.
#
# 예를 들어 3 구(구멍이 세 개 달린) 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면,
#
# 키보드
# 헤어드라이기
# 핸드폰 충전기
# 디지털 카메라 충전기
# 키보드
# 헤어드라이기
# 키보드, 헤어드라이기, 핸드폰 충전기의 플러그를 순서대로 멀티탭에 꽂은 다음 디지털 카메라 충전기 플러그를 꽂기 전에 핸드폰충전기 플러그를 빼는 것이 최적일 것이므로 플러그는 한 번만 빼면 된다.

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
products = list(map(int, input().split()))  # 전기용품 사용 순서
OnUseList = [0] * N # 사용중인 제품 목록
temp = 0
maximum = 0
cnt = 0

while products:
    product = products[0]
    # 만약 해당번호 전기용품을 이미 멀티탭에 꽂아 사용중이라면?
    # 굳이 뺄 필요가 없으므로 그냥 패스한다.
    if product in OnUseList:
        products.remove(product)
        continue
    # 사용중인 제품 목록에 0이 들어있다면? => 아직 아무것도 안 꽂은 상태
    elif 0 in OnUseList:
        OnUseList[OnUseList.index(0)] = product
        products.remove(product)
    # 사용중인 제품 목록이 다 들어찼다면? => 멀티탭이 다 꽂혀져있는 상태
    else:
        # 멀티탭에 꽂혀있는 제품 중 이후에 꽂는 제품이 없는 경우
        # 이후에 꽂는 제품이 없는 제품을 빼주고 탐색중인 제품을 꽂는다.
        for thing in OnUseList:
            if thing not in products:
                temp = thing
                break
        # 멀티탭에 꽂혀있는 제품 중 이후에 꽂는 제품이 있는 경우
        # 멀티탭에 꽂혀있는 제품 중 가장 나중에 사용하는 제품을 고름
        # 가장 나중에 사용하는 제품을 뽑고 탐색하고 있는 제품을 꽂는다.
            elif products.index(thing) > maximum:
                maximum = products.index(thing)
                temp = thing
        OnUseList[OnUseList.index(temp)] = product
        products.remove(product)
        maximum = 0
        # 플러그를 빼는 횟수 1만큼 증가
        cnt += 1
print(cnt)

# 이 문제를 해결하는데만 5시간이 넘게 걸렸다.
# if 분기문에서 가장 마지막 경우를 해결하는데 많은 시간이 걸렸다.
# 다른 사람의 풀이도 참고하고 손으로 그려가면서 힘들게 이해했던 문제였다.



