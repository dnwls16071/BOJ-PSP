# 집합 S는 크기가 N이고, 원소가 문자열인 집합이다. Q개의 문자열이 주어졌을 때, 각 문자열의 부분 문자열이 집합 S에 있는지 판별하는 프로그램을 작성하시오. 문자열의 여러 부분 문자열 중 하나라도 집합 S에 있으면 'YES'를 출력하고, 아무것도 없으면 'NO'를 출력한다.

# 예를 들어, 집합 S = {"www","woo","jun"} 일 때, "myungwoo"의 부분 문자열인 "woo" 가 집합 S에 있으므로 답은 'YES'이고, "hongjun"의 부분 문자열 "jun"이 집합 S에 있으므로 답은 'YES'이다. 하지만, "dooho"는 모든 부분 문자열이 집합 S에 없기 때문에 답은 'NO'이다.

N = int(input())

S = []
for _ in range(N):
    S.append(input())
S = set(S)

M = int(input())

Q = []
for _ in range(M):
    Q.append(input())
Q = set(Q)

for i in S:
    for j in Q:
        if str(j) == j.intersection(i):
            print("YES")
        else:
            print("NO")