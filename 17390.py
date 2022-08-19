# 숭실골 높은 언덕 깊은 골짜기에 출제로 고통 받는 욱제가 살고 있다!

# 욱제는 또 출제를 해야 해서 단단히 화가 났다. 그래서 욱제는 길이 N짜리 수열 A를 만들고, A를 비내림차순으로 정렬해서 수열 B를 만들어 버렸다!! 여기서 B를 출력하기만 하면 문제가 너무 쉬우니까 하나만 더 하자. 아래와 같은 질문이 무려 Q개나 주어진다!! (ㅎㅎ;; ㅈㅅ.. ㅋㅋ!!)

# L R: BL + BL+1 + ... + BR-1 + BR 을 출력한다.

# Figure 1. 모든 참가자가 문제를 풀 수 있을 것이라고 기대하는 욱제의 표정

# 욱제의 질문에 답하고 함께 엠티를 떠나자!!

from itertools import accumulate
input = __import__('sys').stdin.readline

N, Q = map(int, input().split())
A_lst = sorted([*map(int, input().split())])
acc_sum = list(accumulate(A_lst))
acc_sum.insert(0, 0)

for _ in range(Q):
    L, R = map(int, input().split())
    print(acc_sum[R] - acc_sum[L-1])

# 17390(이건 꼭 풀어야 해!) 문제는 누적합 모듈에 대해서 공부할 수 있었다. 
# 반복문으로 합을 누적시켜 계산하는 방법도 있지만 간편하게 from itertools import accumulate를 사용할 수 있다. 
# 누적합 모듈에 대한 부분을 모른 상태에서 풀었을 때는 좀 더 길고 장황한 코드가 나왔지만 모듈을 사용하고 난 후에는 더 효율적인 코드를 작성할 수 있었다.