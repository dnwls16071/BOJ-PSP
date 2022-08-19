# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

# 2차 작성한 코드
import math
A, B, V = map(int, input().split())
day = math.ceil((V-B)/(A-B))
print(day)

# 1차 작성한 코드
# 이 코드가 답이 아닌 이유
# >> 낮에 올라가고 밤에 내려가는 한 주기가 반복되어야 하루가 지나는것
# >> 그렇기에 정확하게 계산을 하면 4일이 아닌 3.x일이 되므로 이걸 올림 해줘야한다.
# 최종 높이는 V - B , 하루 올라간 길이는 A - B
# 최종 높이를 하루 올라간 길이로 나눠주고 올림해야한다.
import sys
input = sys.stdin.readline
A, B, V = map(int, input().split())

day = 0 # V미터에 도달하는데 걸리는 일 수 저장
res = 0 # A미터 올라가고 B미터 내려가고...
while 1:
    res += (A - B)
    if res != V:
        day += 1
    
    if res >= V:
        break
print(day)