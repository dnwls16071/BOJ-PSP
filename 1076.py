# 전자 제품에는 저항이 들어간다. 저항은 색 3개를 이용해서 그 저항이 몇 옴인지 나타낸다. 처음 색 2개는 저항의 값이고, 마지막 색은 곱해야 하는 값이다. 저항의 값은 다음 표를 이용해서 구한다.

# 색	값	곱
# black	0	1
# brown	1	10
# red	2	100
# orange	3	1,000
# yellow	4	10,000
# green	5	100,000
# blue	6	1,000,000
# violet	7	10,000,000
# grey	8	100,000,000
# white	9	1,000,000,000
# 예를 들어, 저항의 색이 yellow, violet, red였다면 저항의 값은 4,700이 된다.

# 내가 작성한 코드(ValueError(런타임에러)가 계속 출력됨)
color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

first, second, third = [input() for _ in range(3)]

result = int(str(color.index(first)) + str(color.index(second))) * (10 ** color.index(third))
print(result)

# 인터넷에서 발췌한 코드
# resistor = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

# first = input()
# second = input()
# third = input()

# value = str(resistor.index(first)) + str(resistor.index(second))

# print(int(value) * (10**resistor.index(third)))