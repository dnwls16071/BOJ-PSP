# 실수 a와 정수 b가 주어졌을 때, a의 b제곱을 정확하게 계산하는 프로그램을 작성하시오.

from decimal import Decimal, getcontext

a, b = map(str, input().split())
getcontext().prec = 3000
print("{0:f}".format(Decimal(a)**int(b)))

# 부동소수점 float는 항상 특정한 값 이하의 오차를 지닌다.
# 파이썬은 15자리의 상대정확도를 가진다.
# 소수점과 같은 부분에서는 정확도가 아주 중요하기 때문에 decimal(소수) 라이브러리를 사용한다.
# getcontext().prec는 정밀도값을 X자리 길이로 설정하는 코드이다.