# 2021년, 홍익대학교는 절대평가를 시행한다. 착한 도현이는 A학점을 받는 사람이 최대한 많았으면 한다.
#
# 시험을 응시한 학생의 수 $N$, 상대평가 시 A학점의 비율 $X\%$와 절대평가 시 A학점을 받기 위한 최소 점수 $Y$점이 주어질 때, 상대평가 시 A학점을 받는 인원의 수와 절대평가 시 A학점을 받는 인원의 수를 구하는 프로그램을 작성해보자.

N = int(input())
lst = list(map(int, input().split()))
X, Y = map(int,input().split())

val1 = round(N * (X / 100))

cnt = 0
for i in lst:
    if i >= Y:
        cnt += 1
print(val1, cnt)

# int, round는 다르다.
# 소수점 형태에서 int를 하게 된다면 소수 부분을 제외한 정수를 리턴한다.
# 소수점 형태에서 round를 하게 된다면 반올림을 하여 정수를 리턴한다.