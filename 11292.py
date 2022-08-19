# 민우는 학창시절 승부욕이 강해서 달리기를 할 때에도 누가 가장 빠른지를 중요하게 생각하고, 시험을 볼 때에도 누가 가장 성적이 높은지를 중요하게 생각한다. 이번에 반에서 키를 측정하였는데, 민우는 마찬가지로 누구의 키가 가장 큰지 궁금해한다. 민우를 도와 가장 키가 큰 사람을 찾아보자.

while True:
    T = int(input())
    if T == 0:
        break
    lst = []
    students = []
    student_height = []
    for _ in range(T):
        student = input().split()
        student[1] = float(student[1])
        student_height.append(student[1])
        students.append(student)

    max_height = max(student_height)
    for student in students:
        if student[1] == max_height:
            print(student[0], end = " ")
    
    students = []
    student_height = []
    print()