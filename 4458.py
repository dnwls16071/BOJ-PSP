# 문장을 읽은 뒤, 줄의 첫 글자를 대문자로 바꾸는 프로그램을 작성하시오.

# 문장 전체 대문자 변환 : upper()
# 문장 전체 소문자 변환 : lower()
# 문장 첫 글자 대문자 변환 : title()

# 문자열은 값 바꾸기가 불가하므로 슬라이싱 개념을 이용하여 이어주면 된다
N = int(input())

for _ in range(N):
    data = str(input())
    data = data[0].upper() + data[1:]
    print(data)