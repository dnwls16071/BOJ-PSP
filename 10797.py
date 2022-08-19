# 서울시는 6월 1일부터 교통 혼잡을 막기 위해서 자동차 10부제를 시행한다. 자동차 10부제는 자동차 번호의 일의 자리 숫자와 날짜의 일의 자리 숫자가 일치하면 해당 자동차의 운행을 금지하는 것이다. 예를 들어, 자동차 번호의 일의 자리 숫자가 7이면 7일, 17일, 27일에 운행하지 못한다. 또한, 자동차 번호의 일의 자리 숫자가 0이면 10일, 20일, 30일에 운행하지 못한다.

# 여러분들은 일일 경찰관이 되어 10부제를 위반하는 자동차의 대수를 세는 봉사활동을 하려고 한다. 날짜의 일의 자리 숫자가 주어지고 5대의 자동차 번호의 일의 자리 숫자가 주어졌을 때 위반하는 자동차의 대수를 출력하면 된다. 

T = int(input()) # 날짜의 일의 자리 숫자가 주어짐
lst = list(map(int, input().split()))   #5대의 자동차 번호를 저장할 리스트 변수 생성

count = 0   # 10부제를 위반한 자동차의 대수를 저장하는 변수
for i in lst:   # lst의 요소를 받아온다
    if T == i:  # 만약 날짜의 일의 자리 숫자와 lst의 요소값이 일치한다면(10부제 위반)
        count += 1  # count값이 1씩 증가됨
print(count)    # count값 출력