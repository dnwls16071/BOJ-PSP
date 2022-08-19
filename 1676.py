# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# 결과값을 10으로 나누었을때 나머지가 0이 나와야한다.
from math import factorial

count = 0
n = factorial(int(input()))
while n % 10 == 0:
    n = n // 10
    count += 1
print(count)