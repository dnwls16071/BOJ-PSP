# 2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

# int(input(), 2) > 2진수로 입력
# oct() > 8진수로 변환

print(oct(int(input(), 2))[2:])