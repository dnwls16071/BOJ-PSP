# 동규는 세수를 하다가 정렬이 하고싶어졌다.
# 숫자 세 개를 생각한 뒤에, 이를 오름차순으로 정렬하고 싶어 졌다.
# 숫자 세 개가 주어졌을 때, 가장 작은 수, 그 다음 수, 가장 큰 수를 출력하는 프로그램을 작성하시오.

number = list(map(int, input().split()))

number.sort()
print(number[0], number[1], number[2])


