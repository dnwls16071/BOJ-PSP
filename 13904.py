# 웅찬이는 과제가 많다. 하루에 한 과제를 끝낼 수 있는데, 과제마다 마감일이 있으므로 모든 과제를 끝내지 못할 수도 있다. 과제마다 끝냈을 때 얻을 수 있는 점수가 있는데, 마감일이 지난 과제는 점수를 받을 수 없다.

# 웅찬이는 가장 점수를 많이 받을 수 있도록 과제를 수행하고 싶다. 웅찬이를 도와 얻을 수 있는 점수의 최댓값을 구하시오.

# 참고하여 작성한 코드
import sys
input = sys.stdin.readline

N = int(input())
homeworks = []
for i in range(N):
    d, w = map(int, input().split())
    homeworks.append((d, w))
homeworks.sort(reverse=True, key=lambda x:x[1])

score = 0
days = [0] * (N+1)
for homework in homeworks:
    for d in range(homework[0], 0, -1):
        if days[d] == 0:
            days[d] = 1
            score += homework[1]
            break
print(score)
            
# 참고한 코드            
import sys
input = sys.stdin.readline

N = int(input())
homeworks = []
for _ in range(N):
    homeworks.append(list(map(int, input().split())))
homeworks.sort(reverse=True, key=lambda x: x[1])

score = 0
days = [0]*1001
for homework in homeworks:
    for d in range(homework[0], 0, -1):
        if days[d] == 0:
            days[d] = 1
            score += homework[1]
            break
print(score)