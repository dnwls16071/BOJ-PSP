# 최백준이 이번 학기에 들은 과목과 학점 그리고 성적이 주어졌을 때, 평균 평점을 계산하는 프로그램을 작성하시오.

# 성적은 A+~F까지 총 13개가 있다.

# A+: 4.3, A0: 4.0, A-: 3.7

# B+: 3.3, B0: 3.0, B-: 2.7

# C+: 2.3, C0: 2.0, C-: 1.7

# D+: 1.3, D0: 1.0, D-: 0.7

# F: 0.0

# 평균 평점은 각 과목의 학점*성적을 모두 더한 뒤에, 총 학점으로 나누면 된다.

# 1차 작성한 코드(말도 안되는 조건문 일일 반복 코드)
from re import L


res = 0
N = int(input())
for i in range(N):
    subject, score, grade = map(str, input().split())
    score = int(score)
    if grade == "A+":
        res += score * 4.3
    elif grade == "A0":
        res += score * 4.0
    elif grade == "A-":
        res += score * 3.7
    elif grade == "B+":
        res += score * 3.3
    elif grade == "B0":
        res += score * 3.0
    elif grade == "B-":
        res += score * 2.7
    elif grade == "C+":
        res += score * 2.3
    elif grade == "C0":
        res += score * 2.0
    elif grade == "C-":
        res += score * 1.7
    elif grade == "D+":
        res += score * 1.3
    elif grade == "D0":
        res += score * 1.0
    elif grade == "D-":
        res += score * 0.7
    else:
        res += score * 0.0
print(round(res/sum(score), 2))

# 2차 작성한 코드(딕셔너리를 이용한 코드)
d = {"A+": 4.3, "A0": 4.0, "A-": 3.7, "B+": 3.3, "B0": 3.0, 
    "B-": 2.7, "C+": 2.3, "C0": 2.0, "C-": 1.7, "D+": 1.3, 
    "D0": 1.0, "D-": 0.7, "F": 0.0}

score_value = 0
grade_value = 0
for i in range(int(input())):
    subject, score, grade = map(str, input().split())
    score = int(score)
    score_value += score
    # 딕셔너리 사용 방법
    # 딕셔너리명[변수] > 대괄호 사용
    grade_value += score * d[grade]
print("%.2f" % (round(grade_value / score_value + 10**-5, 2))) 