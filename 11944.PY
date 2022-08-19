# 문제는 매우 간단하다. N을 N번 출력하는 프로그램을 작성하여라. 다만, 답이 길어지는 경우 답의 앞 M자리만 출력한다.

N, M = map(int, input().split())

print((str(N)*N)[:M])