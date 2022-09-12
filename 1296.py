# 연두는 프로그래밍 대회에 나갈 팀 이름을 정하려고 한다. 미신을 믿는 연두는 이환이에게 공식을 하나 받아왔고, 이 공식을 이용해 우승할 확률이 가장 높은 팀 이름을 찾으려고 한다.
#
# 이환이가 만든 공식은 사용하려면 먼저 다음 4가지 변수의 값을 계산해야 한다.
#
# L = 연두의 이름과 팀 이름에서 등장하는 L의 개수
# O = 연두의 이름과 팀 이름에서 등장하는 O의 개수
# V = 연두의 이름과 팀 이름에서 등장하는 V의 개수
# E = 연두의 이름과 팀 이름에서 등장하는 E의 개수
# 그 다음, 위에서 구한 변수를 다음 식에 입력하면 팀 이름의 우승할 확률을 구할 수 있다.
#
# ((L+O) × (L+V) × (L+E) × (O+V) × (O+E) × (V+E)) mod 100
#
# 연두의 영어 이름과 팀 이름 후보 N개가 주어졌을 때, 우승할 확률이 가장 높은 팀 이름을 구해보자. 확률이 가장 높은 팀이 여러가지인 경우 사전 순으로 가장 앞서는 팀 이름이 우승할 확률이 가장 높은 것이다.

eng_name = input()
N = int(input())
lst = sorted([input() for i in range(N)])
possibilty = 0
result = 0
for i in range(N):
    L = eng_name.count("L") + lst[i].count("L")
    O = eng_name.count("O") + lst[i].count("O")
    V = eng_name.count("V") + lst[i].count("V")
    E = eng_name.count("E") + lst[i].count("E")
    total = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    if possibilty < total:
        possibilty = total
        result = i
print(lst[result])