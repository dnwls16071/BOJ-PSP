# 김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.

# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

N = int(input())

book = {}
for _ in range(N):
    book_name = input()
    if book_name in book:
        book[book_name] += 1    # 책 이름이 딕셔너리에 있으면 1만큼 증가
    else:
        book[book_name] = 1     # 책 이름이 딕셔너리에 없으면 1을 입력하고 추가

lst = []
num = max(book.values())    # 가장 많이 팔린 책 개수

for i in book:
    if num == book[i]:
        lst.append(i)

lst.sort()
print(lst[0])

# 딕셔너리를 이용하는 문제였다.
