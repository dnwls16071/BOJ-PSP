# 주어진 N개의 정수 중에서 양의 정수의 개수를 출력하는 프로그램을 작성하시오.

number = list(map(int, input().split()))

cnt = 0
for i in number:
    if i > 0:
        cnt += 1
    else:
        cnt += 0
print(cnt) 