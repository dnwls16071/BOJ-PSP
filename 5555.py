# 당신은 N개의 반지를 가지고 있다. 각각의 반지는 대문자 10 문자로 이루어진 문자열이 새겨져 있다. 반지는 문자열의 시작과 끝이 연결된 형태로 문자가 새겨져 있다. 반지에 각인된 문자열을 거꾸로 읽는 걱정은 없다.
#
# 찾고자하는 문자열이 주어졌을 때 그 문자열을 포함하는 반지가 몇 개인지를 발견하는 프로그램을 작성하라.

ring_string = input()
N = int(input())
lst = []
for _ in range(N):
    lst.append(input())

cnt = 0
for i in lst:
    i += (i*N)
    if ring_string in i:
        cnt += 1
print(cnt)

# 원형 반지가 순환되므로 원형반지의 문자열을 여러 번 반복했을때 만약 해당 문자열이 들어있으면 카운팅한다.