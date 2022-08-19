 # 준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.
#
# 준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.

N = int(input())
card_dict = {}
for i in range(N):
    card = int(input())
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

# card_dict를 정렬하되, 우선적으로 Value값이 큰 순서대로 정렬하고 Value값이 동일한 경우 Key값이 작은 순서대로 정렬하라는 뜻이다.
result = sorted(card_dict.items(), key = lambda x:(-x[1], x[0]))
print(result[0][0])

# 일일이 브루트포스로 탐색을 하게 된다면 소요되는 시간이 매우 커질 것이다.
# 이 때 딕셔너리 자료형을 이용해서 정리하면 도움이 된다.

# 딕셔너리의 이해
# 딕셔너리의 기본 구조는 {Key1 : Value1, Key2 : Value2, Key3 : Value3...}이다.
# 이 때 Key값은 불변해야하고 Value값은 상관없다.

# 딕셔너리 자료형을 정렬할때 사용하는 파이썬 함수는 sorted입니다.
# 딕셔너리 자료형 중에서 Key값을 정렬하는 방법
# result = sorted(card_dict.items(), key = lambda x : x[0])

# 딕셔너리 자료형 중에서 Value값을 정렬하는 방법
# result = sorted(card_dict.items(), key = lambda x : x[0])

# 매개변수 뒤에 -를 붙이는 것은 내림차순을 의미한다.
# sorted(pi.items(), key=lambda x:(-x[1], x[0])):

