# 대한고등학교에 재학 중인 민국이와 만세는 4과목(정보, 수학, 과학, 영어)에 대한 시험을 봤다. 민국이와 만세가 본 4과목의 점수를 입력하면, 민국이의 총점 S와 만세의 총점 T 중에서 큰 점수를 출력하는 프로그램을 작성하시오. 단, 서로 동점일 때는 민국이의 총점 S를 출력한다.

first_score = list(map(int, input().split()))
second_score = list(map(int, input().split()))

if sum(first_score) > sum(second_score):
    print(sum(first_score))
elif sum(first_score) < sum(second_score):
    print(sum(second_score))
else:
    print(sum(first_score))