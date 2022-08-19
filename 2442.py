# 첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개를 찍는 문제
# 별은 가운데를 기준으로 대칭이어야 한다.
# 출력 형식 오류 > print문에 쉼표를 사용하면 불필요한 공백이 생길 수 있으므로 꼼꼼하게 코드를 작성하는것에 주의하자

N = int(input())

for i in range(1, N+1):
    print(" "*(N-i) + "*"*((2*i)-1))