# 어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.
# 정렬 lambda 함수 사용법(key값을 기준으로 정렬되고 기본값은 오름차순이다.)
# list 자료형에 하나의 값이 아닌 한 세트의 값이 추가되야한다면?
# 리스트명.append([])
# lambda를 이용한 정렬 함수를 사용하려면?
# lst.sort(key=lambda x:x[1]) > 기준값이 한 개인 경우 ()필요X
# lst.sort(key=lambda x:(x[3], x[2], x[1])) > 기준값이 여러 개인 경우 ()필요O
# x[3]의 기준으로 정렬하는데 만약 x[3]의 값이 같으면 x[2]로 비교하는 이런식


n = int(input())

lst = []
for i in range(n):
    name, day, month, year = input().split()
    lst.append([name, int(day), int(month), int(year)])
lst.sort(key=lambda x:(x[3],x[2],x[1]))
print(lst[-1][0])
print(lst[0][0])