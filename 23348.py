# 대한민국 최고의 알고리즘 동아리를 찾기 위한 리얼리티 서바이벌. 잔혹한 코딩판에서 살아남기 위한 대학생들의 자존심을 건 생존 경쟁이 시작된다!

# 스트릿 코딩 파이터는 최근 모임을 갖지 못하게 된 알고리즘 동아리들을 위해 방송사에서 제작한 특별 프로그램이다.

# 참가한 동아리들은 3인 1팀으로 팀을 구성해 각자 라이브로 문제를 풀고 심사를 받는다.

# 심사기준은 정답과 상관없이 멋있게 문제를 푸는 사람들이 유리한 점수를 가져가게 되는데, 이때 점수가 부여되는 공식적인 기술은 '한손 코딩', '노룩 코딩', '폰코딩'으로 총 3가지이고, 각 기술들에는 난이도가 다르게 부여된다.

		
# 한손 코딩	노룩 코딩	폰코딩
# <예시>

# 심사 방식은 다음과 같다.

# 동아리의 총 점수는 구성원들의 개인 점수 합이다.
# 개인 점수는 세 가지 기술 점수의 합이다.
# 기술 점수는 해당 기술의 난이도와 사용한 횟수를 곱한 값이다.
# 예를 들어 '한손 코딩', '노룩 코딩', '폰코딩'의 난이도가 각각 3, 6, 9이며 플레이어 $P$가 위 기술을 각각 1, 2, 3번 보여주었다면, $P$의 점수는 ($3 \times 1$) + ($6 \times 2$) + ($9 \times 3$) = 42점이 된다.

# 기술의 난이도와 동아리 별 각 팀원들이 사용한 기술의 횟수가 주어진다. 가장 높은 점수를 받은 동아리의 점수는 몇 점인지 구하는 프로그램을 작성하시오.

A, B, C = map(int, input().split())
N = int(input())

res = 0
for i in range(N):
    total = 0
    for j in range(3):
        a, b, c = map(int, input().split())
        total += (A*a + B*b + C*c)
    
    res = max(res, total)
print(res)