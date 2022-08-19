# 새 학기를 맞아 상근이는 책을 10권 구입했다. 상근이는 의욕이 너무 앞서서 가격을 조사하지 않고 책을 구입했다. 이제 각 책의 가격을 알아보려고 한다.
# 하지만, 영수증에는 얼룩이 묻어있었고, 상근이는 책 10권 중 9권의 가격만 읽을 수 있었다.
# 책 10권의 총 가격과 가격을 읽을 수 있는 9권 가격이 주어졌을 때, 가격을 읽을 수 없는 책의 가격을 구하는 프로그램을 작성하시오.

total_price = int(input())  # 10권의 총 가격

part_list = []
for i in range(9):
    part_list.append(int(input()))   # 9권의 가격을 입력하여 part_list에 추가

result = total_price - sum(part_list)
print(result)