# IQ Test의 문제 중에는 공통된 패턴을 찾는 문제가 있다. 수열이 주어졌을 때, 다음 수를 찾는 문제이다.
#
# 예를 들어, 1, 2, 3, 4, 5가 주어졌다. 다음 수는 무엇인가? 당연히 답은 6이다. 약간 더 어려운 문제를 보면, 3, 6, 12, 24, 48이 주어졌을 때, 다음 수는 무엇인가? 역시 답은 96이다.
#
# 이제 제일 어려운 문제를 보자.
#
# 1, 4, 13, 40이 주어졌을 때, 다음 수는 무엇일까? 답은 121이다. 그 이유는 항상 다음 수는 앞 수*3+1이기 때문이다.
#
# 은진이는 위의 3문제를 모두 풀지 못했으므로, 자동으로 풀어주는 프로그램을 작성하기로 했다. 항상 모든 답은 구하는 규칙은 앞 수*a + b이다. 그리고, a와 b는 정수이다.
#
# 수 N개가 주어졌을 때, 규칙에 맞는 다음 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
N_lst = list(map(int, input().split()))

if N == 1:
    print("A")
elif N == 2:
    if N_lst[0] == N_lst[1]:
        print(N_lst[0])
    else:
        print("A")
else:
    if N_lst[1] - N_lst[0] == 0:
        a = 0
        b = N_lst[1]
    else:
        a = (N_lst[2]-N_lst[1]) // (N_lst[1]-N_lst[0])
        b = N_lst[1] - N_lst[0] * a

    flag = True # 정수 a, b가 규칙성을 파악하는지 여부를 결정하는 변수 flag
    for i in range(1, N):
        if N_lst[i] == N_lst[i-1] * a + b:
            flag = True
        else:
            flag = False
            print("B")
            break
    if flag == True:
        print(N_lst[-1] * a + b)

# 문제 정답률 보고 경악했지만 의외로 쉬워보여서 도전했던 문제였다.
# 게시판에 있던 반례들과 테스트케이스들을 모두 적용해서 적어가며 코딩했던 문제였다.

