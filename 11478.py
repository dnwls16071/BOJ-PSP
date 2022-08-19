# 문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.
#
# 부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.
#
# 예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.

S = input()
ans = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        temp = S[i:j+1]
        ans.add(temp)
print(len(ans))

# 자료형으로 집합을 사용하면 중복되는걸 거를 수 있기 때문에 리스트를 사용해서 조건문을 돌리는것보다 효율적이다.
# 이 문제를 해결하다가 궁금증이 생겨 백준 게시판에도 질문을 남겼었다.

# import sys를 사용한 결과 답은 18이 출력되었는데 라이브러리를 사용하지 않은 경우에는 답이 정상적으로 12가 출력되었다.
# sys.stdin.readline은 input보다 빠른 입출력 형식이라는 점만 알고 있으면 될 것 같다.
# sys 라이브러리를 사용했을 때 틀린 답이 출력되는 이유는 sys.stdin.readline이 개행문자가 입력받는 입력 형식이기 때문이다.

# ex. input을 사용하여 입력을 받으면 S는 'ababc'가 되어 len(S) = 5가 된다.
# ex. sys.stdin.readline을 사용하여 입력을 받으면 S는 'ababc\n'이 되어 len(S) = 7이 된다.
