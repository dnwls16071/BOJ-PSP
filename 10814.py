# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

N = int(input())

member_list = []
for i in range(N):
    member_age, member_name = list(map(str, input().split()))
    member_age = int(member_age)
    member_list.append(member_age, member_name)

member_list.sort(key = lambda member : (member[0]))

for member in member_list:
    print(member[0], member[1])