# 상근이는 보통 사람들이 사는 것과는 조금 다른 삶을 사는 사람이다. 상근이는 이런 사람들의 시선이 부담스럽기 때문에, 자신만의 숫자를 개발하기로 했다. 바로 그 이름은 팩토리얼 진법이다. 팩토리얼 진법은 각 자리에 올 수 있는 숫자는 0부터 9까지로 10진법과 거의 비슷하다. 하지만, 읽는 법은 조금 다르다. 팩토리얼 진법에서는 i번 자리의 값을 ai×i!로 계산한다. 즉, 팩토리얼 진법에서 719는 10진법에서 53과 같다. 그 이유는 7×3! + 1×2! + 9×1! = 53이기 때문이다.

# 팩토리얼 진법으로 작성한 숫자가 주어졌을 때, 10진법으로 읽은 값을 구하는 프로그램을 작성하시오. 

# 1차 작성한 코드(헷갈려하고 쉬운 부분에서 답을 찾지 못했던 코드)
# 시간초과가 발생했던 코드
# from math import factorial

# while 1:
#     num = str(input())
#     if int(num) == 0:
#         break
    
#     lst = []
#     res = 0
#     for i in range(len(num)):
#         res += int(num[i])* int(factorial(len(num) - i))
#     lst.append(res)

#     for j in lst:
#         print(j)

# 2차 재작성한 코드
# sys 모듈을 사용하였고 rstrip()를 곁들여 사용
import sys
# math 라이브러리에서 factorial 모듈을 사용
from math import factorial

while 1:
    num = sys.stdin.readline().rstrip()
    if int(num) == 0:
        break
    
    res = 0
    for i in range(len(num)):
        res += int(num[i]) * int(factorial(len(num) - i))
    print(res)