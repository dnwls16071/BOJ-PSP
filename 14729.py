# 조(Joe)는 중앙대학교 교수이고, 논리회로 설계 과목을 담당하고 있다. 그는 수업을 하면서 7명의 학생을 제외한 나머지 학생들에게 좋은 학점을 주겠다고 약속을 하였다.

# Joe 교수님을 돕기 위해서 학생들의 최종 성적이 주어질 때, 그의 연구실인 You See Lab으로 데려갈 성적이 좋지 못한 7명의 학생, 칠무해의 성적을 뽑아보자.
import sys
input = sys.stdin.readline

N = int(input())
score = []
for _ in range(N):
    score.append(float(input()))
score.sort()

result = []
for idx, val in enumerate(score):
    if idx + 1 > 7:
        break
    result.append(val)

for i in result:
    print('{0:.3f}'.format(i))

# 14729(칠무해) 문제는 매우 간단하게 해결하였다. 
# 이 역시 enumerate()를 사용하여 일종의 예외처리 개념을 사용하였고 소수점 세 자리로 나타내는 형식을 지정해주어 format()을 사용하였다. 
# ★ 소수점을 지정해주는 방식 : round, format 등등...