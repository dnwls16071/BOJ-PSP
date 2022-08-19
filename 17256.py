# 냉장고에서 맛있게 숙성되고 있는 마카롱은 심심한 나머지 새로운 수 체계를 생각해냈다. 마카롱은 이를 케이크 수라고 이름 붙이고, 다음과 같이 정의했다.

# 케이크 수는 3개의 자연수 x, y, z로 이루어진 순서쌍이다. (자연수는 1 이상의 정수를 의미한다)
# 케이크 수 a는 (a.x, a.y, a.z)와 같이 나타낼 수 있다.
# 또한 마카롱은 케이크 수들을 비교하기 위해 등호 "="도 새로 정의했다.

# 케이크 수 a, b에 대하여, a = b라는 것은 다음과 같다.
# a.x = b.x, a.y = b.y 그리고 a.z = b.z를 동시에 만족한다.
# 아직 끝나지 않았다. 이 케이크 수는 기존의 수와 다르게 매우 특이한 연산을 적용할 수 있다. 연산의 이름은 🍰이고 다음과 같이 정의된다!

# a 🍰 b = (a.z + b.x, a.y × b.y, a.x + b.z)

# 케이크와 마카롱 사진

# SCCC의 회장 욱제는 케이크 수를 이용해 문제를 만들기로 했다. 마카롱과 욱제를 기쁘게 하기 위해서 문제를 풀어주자! 욱제가 만든 문제는 다음과 같다.

# 케이크 수 a, c 가 주어졌을 때, 다음을 만족하는 케이크 수 b를 계산하자.

# a 🍰 b = c

# a, c는 b가 항상 유일하게 존재하도록 주어진다.

a_x, a_y, a_z = map(int, input().split())
c_x, c_y, c_z = map(int, input().split())

b_x = c_x - a_z
b_y = c_y // a_y
b_z = c_z - a_x

print(b_x, b_y, b_z)