# 평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.

# 이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.

# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

T = int(input())    # 테스트케이스의 개수
for _ in range(T):  
    floor = int(input())    # 층수
    number = int(input())   # 호수
    lst = [f0 for f0 in range(1, number+1)]
    for _ in range(floor):  # 층수만큼 반복
        for i in range(1, number):
            lst[i] += lst[i-1]
    print(lst[number-1])
    

# 누적합을 사용할 수 있지 않을까...?
from itertools import accumulate

T = int(input())
for _ in range(T):
    floor = int(input())
    number = int(input())
    lst = [f0 for f0 in range(1, number+1)]
    for _ in range(floor):
        lst = list(accumulate(lst))
    print(lst[number-1])

# (2). 2775(부녀회장이 될테야) 문제를 보고 두 가지 풀이법을 생각해냈다. 
# 하나는 층수만큼 반복해서 반복문을 돌려 리스트를 갱신하는 방법이고 또 하나는 from itertools import accumulate 즉, 누적합 모듈을 사용하는 방법이다. 
# 모듈을 사용하면 간편하게 작성할 수 있지만 기업 코딩테스트에서 요하는 문제는 직접 증명이 요구되기에 이런 방법이 있다는 정도만 알아두면 괜찮을 것 같다.