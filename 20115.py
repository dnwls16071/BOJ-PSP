# JOI 상사는 직원의 근무시간을 타임 카드로 관리하고있다. 직원들은 전용 장비를 사용하여 타임 카드에 출근 시간을 기록한다. 근무를 마치고 퇴근할 때도 타임 카드에 퇴근 시간을 기록한다. 타임카드에서 사용하는 시간단위는 24 시간제를 사용한다.

# 보안상의 이유로 직원들의 출근 시간은 7시 이후이다. 또한, 모든 직원은 23시 이전에 퇴근한다. 직원의 퇴근 시간은 항상 출근 시간보다 늦다.

# 입력으로 JOI 상사의 3 명의 직원 A 씨, B 씨, C 씨의 출근 시간과 퇴근 시간이 주어 졌을 때 각 직원의 근무시간을 계산하는 프로그램을 작성하라.

# 시간 문제의 해결팁 : 뒤의 시간에서 앞의 시간을 빼주는 경우 물론 작은 단위의 숫자부터 빼주면서 계산하면 가능하지만 자칫하면 복잡할 수도 있다는 점에서 착안
# 시간에 해당하는 단위면 초로 바꿔서 3600을 곱하고, 분에 해당하는 단위면 초로 바꿔서 60을 곱하고 초에 해당하는 단위면 그대로 가져온다.

for i in range(3):
    a, b, c, d, e, f = map(int, input().split())

    time = ((d * 3600 + e * 60 + f) - (a * 3600 + b * 60 + c))
    print(time // 3600, (time % 3600) // 60, (time % 3600) % 60)