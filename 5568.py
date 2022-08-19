# 상근이는 카드 n(4 ≤ n ≤ 10)장을 바닥에 나란히 놓고 놀고있다. 각 카드에는 1이상 99이하의 정수가 적혀져 있다. 상근이는 이 카드 중에서 k(2 ≤ k ≤ 4)장을 선택하고, 가로로 나란히 정수를 만들기로 했다. 상근이가 만들 수 있는 정수는 모두 몇 가지일까?
#
# 예를 들어, 카드가 5장 있고, 카드에 쓰여 있는 수가 1, 2, 3, 13, 21라고 하자. 여기서 3장을 선택해서 정수를 만들려고 한다. 2, 1, 13을 순서대로 나열하면 정수 2113을 만들 수 있다. 또, 21, 1, 3을 순서대로 나열하면 2113을 만들 수 있다. 이렇게 한 정수를 만드는 조합이 여러 가지 일 수 있다.
#
# n장의 카드에 적힌 숫자가 주어졌을 때, 그 중에서 k개를 선택해서 만들 수 있는 정수의 개수를 구하는 프로그램을 작성하시오.

from itertools import permutations

n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]

res = set()
for val in permutations(cards, k):
    res.add(''.join(list(map(str, val))))
print(len(res))

# join 함수는 리스트 자료형에서만 사용되는 함수다. 따라서 join 함수를 사용하려면 리스트로 변형시켜줘야한다.
# join 함수는 반드시 '문자열' 사이를 구분하기 위한 구분자를 지정, 아무것도 입력하고 싶지 않다면 공백을 넣는다.
# join 함수는 모든 반복 자료형의 데이터를 하나의 '문자열'로 합쳐서 취급한다.

