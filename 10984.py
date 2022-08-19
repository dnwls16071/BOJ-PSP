# 게으른 근우는 열심히 놀다가 문득, 자신의 학점 평균이 얼마일지 궁금해졌다. 학사시스템도 들어가기 귀찮아하는 근우를 위해 구해주도록 하자. 

T = int(input())    #학기의 수 T가 주어진다.

grade = 0
for i in range(T):  #각 학기에 대한 정보 반복
    N = int(input())    #들었던 과목의 수
    total_credit = 0
    total_grade=0

    for i in range(N):  #들었던 과목 수 반복
        credit, grade = map(float, input().split())  #학점과 성적이 주어진다
        total_credit += credit
        total_grade += credit * grade
    
    GPA = total_grade / total_credit
    print(int(total_credit), round(GPA,1))
        